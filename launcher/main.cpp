#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <SDL.h>
#include <SDL_image.h>
#include <SDL_mixer.h>
#include <SDL_ttf.h>
#include <sstream>
#include <string>
#include <vector>
#include <windows.h>

using namespace std;

string GetConfigValue(const string & configPath, const string & key)
{
	ifstream file(configPath);
	string line;
	while (getline(file, line))
	{
		if (line.find(key + "=") == 0)
			return line.substr(key.length() + 1);
	}
	return "";
}

void DrawGlowRect(SDL_Renderer * renderer, SDL_Rect rect, SDL_Color color, int layers)
{
	SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
	for (int i = layers; i >= 0; i--)
	{
		Uint8 alpha = (Uint8) (40 - i * 4);
		SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, alpha);
		SDL_Rect glow = { rect.x - i, rect.y - i, rect.w + i * 2, rect.h + i * 2 };
		SDL_RenderDrawRect(renderer, &glow);
	}
}

void DrawButton(SDL_Renderer * renderer, TTF_Font * font, SDL_Rect rect, const char * label, bool hovered, float alpha)
{
	SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
	Uint8 a = (Uint8) (255 * alpha);

	if (hovered)
	{
		SDL_SetRenderDrawColor(renderer, 0, 255, 70, (Uint8) (30 * alpha));
		SDL_RenderFillRect(renderer, &rect);
		SDL_Color glowColor = { 0, 255, 70, a };
		DrawGlowRect(renderer, rect, glowColor, 6);
		SDL_SetRenderDrawColor(renderer, 0, 255, 70, a);
	}
	else
	{
		SDL_SetRenderDrawColor(renderer, 0, 0, 0, (Uint8) (140 * alpha));
		SDL_RenderFillRect(renderer, &rect);
		SDL_SetRenderDrawColor(renderer, 0, 180, 60, (Uint8) (160 * alpha));
	}
	SDL_RenderDrawRect(renderer, &rect);

	if (font)
	{
		SDL_Color textColor = hovered
			? SDL_Color{ 0, 255, 70, a }
		: SDL_Color{ 0, 180, 60, (Uint8) (200 * alpha) };
		SDL_Surface * surface = TTF_RenderText_Blended(font, label, textColor);
		if (surface)
		{
			SDL_Texture * texture = SDL_CreateTextureFromSurface(renderer, surface);
			SDL_SetTextureAlphaMod(texture, a);
			int tw = surface->w, th = surface->h;
			SDL_Rect textRect = {
				rect.x + (rect.w - tw) / 2,
				rect.y + (rect.h - th) / 2,
				tw, th
			};
			SDL_RenderCopy(renderer, texture, NULL, &textRect);
			SDL_DestroyTexture(texture);
			SDL_FreeSurface(surface);
		}
	}
}

void DrawScanlines(SDL_Renderer * renderer, int winW, int winH)
{
	SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 35);
	for (int y = 0; y < winH; y += 3)
		SDL_RenderDrawLine(renderer, 0, y, winW, y);
}

void DrawVignette(SDL_Renderer * renderer, int winW, int winH)
{
	SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
	for (int i = 0; i < 80; i++)
	{
		SDL_SetRenderDrawColor(renderer, 0, 0, 0, (Uint8) (i * 1.8f));
		SDL_Rect r = { i, i, winW - i * 2, winH - i * 2 };
		SDL_RenderDrawRect(renderer, &r);
	}
}

void DrawGlitch(SDL_Renderer * renderer, int winW, int winH, float intensity)
{
	if (intensity <= 0.0f) return;
	SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
	int lines = (int) (intensity * 6);
	for (int i = 0; i < lines; i++)
	{
		int y = rand() % winH;
		int h = rand() % 4 + 1;
		int offset = (rand() % 20 - 10);
		SDL_SetRenderDrawColor(renderer, 0, 255, 70, (Uint8) (rand() % 80 + 20));
		SDL_Rect glitch = { offset, y, winW, h };
		SDL_RenderFillRect(renderer, &glitch);
	}
}

void DrawTypingTitle(SDL_Renderer * renderer, TTF_Font * font, const string & fullText,
	int charsVisible, bool showCursor, int winW, int y)
{
	if (!font) return;
	string visible = fullText.substr(0, charsVisible);
	if (showCursor) visible += "_";
	SDL_Color color = { 0, 255, 70, 255 };
	SDL_Surface * surface = TTF_RenderText_Blended(font, visible.c_str(), color);
	if (!surface) return;
	SDL_Texture * texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_Rect dst = { (winW - surface->w) / 2, y, surface->w, surface->h };
	SDL_RenderCopy(renderer, texture, NULL, &dst);
	SDL_DestroyTexture(texture);
	SDL_FreeSurface(surface);
}

int main(int argc, char * argv[])
{
	SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO);

	HANDLE mutex = CreateMutexA(NULL, TRUE, "EnemyOfTheStateMutex");
	if (GetLastError() == ERROR_ALREADY_EXISTS)
	{
		MessageBoxA(NULL, "Game already started!", "Enemy Of The State", MB_OK | MB_ICONERROR);
		CloseHandle(mutex);
		return 1;
	}

	IMG_Init(IMG_INIT_PNG | IMG_INIT_JPG);
	TTF_Init();
	Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048);

	char basePath[MAX_PATH];
	GetModuleFileNameA(NULL, basePath, MAX_PATH);
	string exeDir = string(basePath);
	exeDir = exeDir.substr(0, exeDir.find_last_of("\\/"));

	string configPath = exeDir + "\\assets\\config.ini";
	string renpyPath = GetConfigValue(configPath, "renpy");
	string gamePath = GetConfigValue(configPath, "game");

	if (renpyPath.empty() || gamePath.empty())
	{
		MessageBoxA(NULL, "Couldn't find config.ini or the file is empty!\nCheck: assets/config.ini", "Error", MB_OK | MB_ICONERROR);
		Mix_CloseAudio();
		return 1;
	}

	DWORD attr = GetFileAttributesA(renpyPath.c_str());
	if (attr == INVALID_FILE_ATTRIBUTES)
	{
		string msg = "renpy.exe not found at:\n" + renpyPath + "\n\nCheck your config.ini";
		MessageBoxA(NULL, msg.c_str(), "Error", MB_OK | MB_ICONERROR);
		Mix_CloseAudio();
		return 1;
	}

	DWORD gameAttr = GetFileAttributesA(gamePath.c_str());
	if (gameAttr == INVALID_FILE_ATTRIBUTES || !(gameAttr & FILE_ATTRIBUTE_DIRECTORY))
	{
		string msg = "Game folder not found at:\n" + gamePath + "\n\nCheck your config.ini";
		MessageBoxA(NULL, msg.c_str(), "Error", MB_OK | MB_ICONERROR);
		Mix_CloseAudio();
		return 1;
	}

	string launchCmd = "\"" + renpyPath + "\" \"" + gamePath + "\" run";

	SDL_Window * window = SDL_CreateWindow(
		"Enemy Of The State",
		SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
		800, 600, SDL_WINDOW_SHOWN
	);
	SDL_Renderer * renderer = SDL_CreateRenderer(window, -1,
		SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);

	string bgPath = exeDir + "\\assets\\background.png";
	SDL_Texture * background = IMG_LoadTexture(renderer, bgPath.c_str());
	if (!background)
	{
		MessageBoxA(NULL, "background.png not found!", "Error", MB_OK | MB_ICONERROR);
		Mix_CloseAudio();
		return 1;
	}

	string fontPath = exeDir + "\\assets\\font.ttf";
	TTF_Font * fontSmall = TTF_OpenFont(fontPath.c_str(), 16);
	TTF_Font * fontTitle = TTF_OpenFont(fontPath.c_str(), 28);
	if (!fontSmall || !fontTitle)
	{
		string err = "Font not found at:\n" + fontPath;
		MessageBoxA(NULL, err.c_str(), "Font Error", MB_OK | MB_ICONERROR);
		Mix_CloseAudio();
		return 1;
	}

	string typingSoundPath = exeDir + "\\assets\\click.wav";
	Mix_Chunk * typingSound = Mix_LoadWAV(typingSoundPath.c_str());

	if (!typingSound)
	{
		string err = "Sound not found:\n" + typingSoundPath + "\n\nSDL_mixer error: " + Mix_GetError();
		MessageBoxA(NULL, err.c_str(), "Sound Error", MB_OK | MB_ICONWARNING);
	}

	int imgW, imgH;
	SDL_QueryTexture(background, NULL, NULL, &imgW, &imgH);
	int winW = 800, winH = 600;
	float scale = min((float) winW / imgW, (float) winH / imgH);
	int newW = (int) (imgW * scale);
	int newH = (int) (imgH * scale);
	SDL_Rect bgDst = { (winW - newW) / 2, (winH - newH) / 2, newW, newH };

	const char * labels[3] = { "> LAUNCH", "> SETTINGS", "> EXIT" };
	struct Button { SDL_Rect rect; bool isHovered; };
	Button buttons[3] = {
		{{300, 340, 200, 45}, false},
		{{300, 400, 200, 45}, false},
		{{300, 460, 200, 45}, false},
	};

	const string titleText = "ENEMY OF THE STATE";
	int titleChars = 0;
	Uint32 lastCharTime = SDL_GetTicks();
	Uint32 lastCursorBlink = SDL_GetTicks();
	bool cursorVisible = true;
	bool typingDone = false;

	float buttonAlpha[3] = { 0.0f, 0.0f, 0.0f };
	Uint32 buttonFadeStart[3] = { 2000, 2300, 2600 };

	float glitchIntensity = 0.0f;
	Uint32 nextGlitch = SDL_GetTicks() + 3000 + rand() % 4000;

	bool running = true;
	SDL_Event event;

	while (running)
	{
		Uint32 now = SDL_GetTicks();
		int mouseX, mouseY;
		SDL_GetMouseState(&mouseX, &mouseY);

		if (!typingDone && now - lastCharTime > 80)
		{
			titleChars++;
			lastCharTime = now;
			if (typingSound && Mix_Playing(0) == 0)
				Mix_PlayChannel(0, typingSound, 0);
			if (titleChars >= (int) titleText.size())
				typingDone = true;
		}

		if (now - lastCursorBlink > 500)
		{
			cursorVisible = !cursorVisible;
			lastCursorBlink = now;
		}

		for (int i = 0; i < 3; i++)
		{
			if (now > buttonFadeStart[i])
			{
				float t = (now - buttonFadeStart[i]) / 600.0f;
				buttonAlpha[i] = min(1.0f, t);
			}
		}

		if (now >= nextGlitch)
		{
			glitchIntensity = 1.0f;
			nextGlitch = now + 3000 + rand() % 5000;
		}
		if (glitchIntensity > 0.0f)
			glitchIntensity -= 0.08f;

		while (SDL_PollEvent(&event))
		{
			if (event.type == SDL_QUIT) running = false;

			if (event.type == SDL_MOUSEBUTTONDOWN)
			{
				if (buttons[0].isHovered)
				{
					running = false;
					SDL_DestroyTexture(background);
					TTF_CloseFont(fontSmall);
					TTF_CloseFont(fontTitle);
					SDL_DestroyRenderer(renderer);
					SDL_DestroyWindow(window);
					Mix_FreeChunk(typingSound);
					Mix_CloseAudio();
					IMG_Quit(); TTF_Quit(); SDL_Quit();

					STARTUPINFOA si = { sizeof(si) };
					PROCESS_INFORMATION pi;
					char cmd[1024];
					strcpy_s(cmd, launchCmd.c_str());
					CreateProcessA(NULL, cmd, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi);

					Sleep(2000);
					HWND gameWindow = NULL;
					for (int i = 0; i < 10; i++)
					{
						gameWindow = FindWindowA(NULL, "Enemy Of The State");
						if (gameWindow) break;
						Sleep(500);
					}
					if (gameWindow)
					{
						ShowWindow(gameWindow, SW_RESTORE);
						SetForegroundWindow(gameWindow);
						SetFocus(gameWindow);
					}
					CloseHandle(pi.hProcess);
					CloseHandle(pi.hThread);
					CloseHandle(mutex);
					return 0;
				}

				if (buttons[1].isHovered)
					SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, "Settings", "Coming soon...", window);

				if (buttons[2].isHovered)
				{
					SDL_DestroyTexture(background);
					TTF_CloseFont(fontSmall);
					TTF_CloseFont(fontTitle);
					SDL_DestroyRenderer(renderer);
					SDL_DestroyWindow(window);
					Mix_FreeChunk(typingSound);
					Mix_CloseAudio();
					CloseHandle(mutex);
					IMG_Quit(); TTF_Quit(); SDL_Quit();
					return 0;
				}
			}
		}

		for (auto & btn : buttons)
		{
			SDL_Point point = { mouseX, mouseY };
			btn.isHovered = SDL_PointInRect(&point, &btn.rect);
		}

		SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
		SDL_RenderClear(renderer);
		SDL_RenderCopy(renderer, background, NULL, &bgDst);
		DrawScanlines(renderer, winW, winH);

		SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
		SDL_SetRenderDrawColor(renderer, 0, 0, 0, 100);
		SDL_Rect overlay = { 0, 0, winW, winH };
		SDL_RenderFillRect(renderer, &overlay);

		DrawGlitch(renderer, winW, winH, glitchIntensity);
		DrawTypingTitle(renderer, fontTitle, titleText, titleChars,
			typingDone ? cursorVisible : true, winW, 60);

		for (int i = 0; i < 3; i++)
			DrawButton(renderer, fontSmall, buttons[i].rect, labels[i],
				buttons[i].isHovered, buttonAlpha[i]);

		DrawVignette(renderer, winW, winH);
		SDL_RenderPresent(renderer);
	}

	SDL_DestroyTexture(background);
	TTF_CloseFont(fontSmall);
	TTF_CloseFont(fontTitle);
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	Mix_FreeChunk(typingSound);
	Mix_CloseAudio();
	IMG_Quit(); TTF_Quit(); SDL_Quit();
	return 0;
}