from manim import *
from Head import *

"""
TODO
1. write to tape

"""


tapeList = ["b","b","1","1","1","b","b","b","b"]
tape = Table([tapeList], include_outer_lines=True)
tape.get_vertical_lines()[0].set_color(BLACK)
tape.get_vertical_lines()[1].set_color(BLACK)
headObj = Head(tape, position=(1,3))

class TapeAndHead(Scene):

    # class head:
    def move_left(self):
        headObj.move_left()
        head = headObj.get_head()
        pos = head.location
        cell = tape.get_cell(pos)
        arrow = head.arrow
        self.play(arrow.animate.next_to(cell,UP))

    def move_right(self):
        headObj.move_right()
        head = headObj.get_head()
        pos = head.location
        cell = tape.get_cell(pos)
        arrow = head.arrow
        self.play(arrow.animate.next_to(cell,UP))

    def write_to_tape(self, alpha):
        global tape
        global tapeList
        curr_head_pos = headObj.location
        print(curr_head_pos)
        tapeList[curr_head_pos[1]-1] = alpha
        print(tapeList)
        tape2 = Table([tapeList], include_outer_lines=True)
        tape2.get_vertical_lines()[0].set_color(BLACK)
        tape2.get_vertical_lines()[1].set_color(BLACK)
        self.play(Transform(tape,tape2))
        self.remove(tape)
        self.add(tape2)
        tape = tape2

    # def tell_me_what_to_do(self, program, state, curr_alpha):
    #     return program["delta"][state][curr_alpha]

    def construct(self):


        self.add(tape,headObj.get_head().arrow)
        program = {
            "initial" :"q0",
            "final" : ["q3"],
            "delta" : {"q0":
                      {
                      "1":["q0", "x", "R" ], 
                      "b": ["q1", "b", "L"]
                      },
                    "q1":
                     {
                       "1":["q1", "1", "L"],
                       "x":["q2", "1", "R"],
                       "b":["q3", "b", "R"]
                     },  
                     "q2":
                     {
                         "1":["q2", "1", "R"],
                         "b":["q1", "1", "L"]
                     }
                   }
                }

        control_state = program["initial"]
        while(control_state not in program["final"]):
            loc = headObj.location
            ent = str(tape.get_entries(loc).lines_text.original_text)
            
            # try:
            #     l = program["delta"][control_state][ent]
            # except Exception:
            #     break
            l = program["delta"][control_state][ent]
            control_state = l[0]
            self.write_to_tape(l[1])
            if (l[2] == "L"):
                self.move_left()
            else:
                self.move_right()
          
          
            


        # loc = headObj.location
        # cell = tape.get_cell(loc)
        # pprint
        # print()
        # self.move_right()
        # self.move_left()
        # self.write_to_tape("k")
        # self.move_right()
        # self.write_to_tape("x")
        # self.move_right()
        # self.write_to_tape("y")
        # self.wait(1)
        

        # head = headObj.get_head()

        # headObj.move_right()

        # ent = tape.get_entries()
        # for item in ent:
        #         print(item.
        # cell_last = tape.get_cell((1,4))
        # cell_first = tape.get_cell((1,1))
        # cell_2 = tape.get_cell(cell_first.get_center)

        # for i in [(1,1),(1,2),(1,3),(1,4)]:
        #     if cell_first == tape.get_cell((i)):
        #           print("yes found it")

        # print(cell_first.get)
        # print(cell_first.points)
        # print(cell_first.get)
        # print(cell_first)

        # headObj = Head(cell_first)
        # head = headObj.get_head()
        # self.add(tape, head)

        # head.next_to(cell_first, UP)
        # head_location = cell_first
        # t0.get_vertical_lines()[1].set_color(BLACK)
        

        # arrow_1.move_to(cell, UP)
        # self.add(tape,head)
        # self.play(head.animate.next_to(cell_last,UP))
        # self.wait(1)
         
        # self.play(Create(Arrow(start=UP, end=DOWN, color=GOLD).next_to(cell,UP)))
        
        # self.add(circle, square, triangle)
        # self.wait(1)

        
        
        
        
        
        # circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        # square = Square()  # create a square
        # square.rotate(PI / 4)  # rotate a certain amount

        # self.play(Create(square))  # animate the creation of the square
        # self.play(Transform(square, circle))  # interpolate the square into the circle
        # self.play(FadeOut(square))  # fade out animation


        # rectangle = Rectangle()  # create a circle
        # rect1 = Rectangle(width=4.0, height=1.0, grid_xstep=1.0)
        # head = Arrow(start=UP, end=DOWN, color=GOLD)
        # arrow_1.next_to(rect1, UP)

        # self.add(rect1)
        # self.add(arrow_1)
        # what do I want
        # 1. I need to write in the squares
        # 2. I also need to move the arrow to the squares
        # 3. Remove the right boundary of the rectangle
        # print("Hello")