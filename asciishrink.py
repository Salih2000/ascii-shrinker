def shrink_ascii(ascii_art, scale_factor):
   
    lines = ascii_art.split('\n')
    new_lines = []
    for i in range(0, len(lines), int(1/scale_factor)):
        new_line = ""
        for j in range(0, len(lines[i]), int(1/scale_factor)):
            new_line += lines[i][j]
        new_lines.append(new_line)
    return '\n'.join(new_lines)

ascii_art = """
  Paste your ASCII art here
"""
shrunken_ascii = shrink_ascii(ascii_art, 0.5)
print(shrunken_ascii)
