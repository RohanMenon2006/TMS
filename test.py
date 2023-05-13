for teacher in teachers:
    checkbox = CheckBox(frame, text=teacher)
    checkbox.pack(side=LEFT)
    
    if index % 8 == 0 and index > 0:
        checkbox_frames.append(frame)
        frame = Frame(root)
    
    index += 1
    
for frame in checkbox_frames:
    frame.pack()