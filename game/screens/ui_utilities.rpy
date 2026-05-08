################################################################################
## UI_UTILITIES.RPY — Shared Displayable Classes and Helpers
## Classified: The Snowden Files
## 
## Consolidated utilities for all UI screens including:
##   - TypedText: Character-by-character text reveal animation
##   - ScanlineOverlay: CRT monitor scanline effect
##   - RedScanlineOverlay: Red-tinted scanline effect for danger states
################################################################################

init python:
    class TypedText(renpy.Displayable):
        """Reveals text character by character with configurable speed."""
        def __init__(self, text, font, size, color, reveal_speed=0.04, **kwargs):
            super(TypedText, self).__init__(**kwargs)
            self.text = text
            self.font = font
            self.size = size
            self.color = color
            self.reveal_speed = reveal_speed
            
        def render(self, width, height, st, at):
            # Calculate how many characters should be revealed based on time
            revealed_chars = int(st / self.reveal_speed)
            if revealed_chars > len(self.text):
                revealed_chars = len(self.text)
            
            # Get the text to display
            display_text = self.text[:revealed_chars]
            
            # Create text displayable and render it
            text_obj = Text(display_text, font=self.font, size=self.size, color=self.color)
            return text_obj.render(width, height, st, at)
        
        def visit(self):
            return []


    class ScanlineOverlay(renpy.Displayable):
        """Creates a scanline effect overlay to simulate CRT monitor."""
        def __init__(self, width, height, line_spacing=3, line_width=2, **kwargs):
            super(ScanlineOverlay, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.line_spacing = line_spacing
            self.line_width = line_width
        
        def render(self, width, height, st, at):
            r = renpy.Render(int(self.width), int(self.height))
            c = r.canvas()
            
            # Draw horizontal scanlines with neutral black
            color = (0, 0, 0, 30)  # Semi-transparent black
            for y in range(0, int(self.height), self.line_spacing):
                c.line(color, (0, y), (int(self.width), y), self.line_width)
            
            return r
        
        def visit(self):
            return []


    class RedScanlineOverlay(renpy.Displayable):
        """Creates a red-tinted scanline effect overlay for game over state."""
        def __init__(self, width, height, line_spacing=3, line_width=2, **kwargs):
            super(RedScanlineOverlay, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.line_spacing = line_spacing
            self.line_width = line_width
        
        def render(self, width, height, st, at):
            r = renpy.Render(int(self.width), int(self.height))
            c = r.canvas()
            
            # Draw horizontal scanlines with red tint
            color = (139, 0, 0, 40)  # Dark red with transparency
            for y in range(0, int(self.height), self.line_spacing):
                c.line(color, (0, y), (int(self.width), y), self.line_width)
            
            return r
        
        def visit(self):
            return []
