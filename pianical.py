from pygame import mixer
mixer.init()
from tkinter import *
root=Tk()
root.title("PIANICAL")
root.geometry('1360x700')
#root.iconbitmap('piano.ico')
main_frame=Frame(root,background='#b53b35')
main_frame.place(x=0,y=0,height=700,width=1360)
orig_color='SystemButtonFace'
print("#DEVELOPER CONTACT : +919773211427")
print("#MAIL 1            : johntygomes30@gmail.com")
print("#MAIL 2            : guitaricals@gmail.com")
#######  Major Frame and Minor   #####
frame_major=Frame(main_frame,background='#b53b35')
frame_major.place(x=0,y=50,width=1355,height=130)
major_scale_label=Label(frame_major,text='Major and Minor Scale Notes',font=40,background='#b53b35',foreground='white')
major_scale_label.place(x=0,y=0)
#######   Scale Label  ######
scale_label=Label(main_frame,text='Scale Notes',font=40)
scale_label.place(x=1330/2,y=0)
######   Find Chords in Your Scale   #######
frame_chord=Frame(main_frame,background='black')
frame_chord.place(x=0,y=170,width=1355,height=100)
minor_scale_label=Label(frame_chord,text='Chords',font=40)
minor_scale_label.place(x=0,y=0)
orig_color = minor_scale_label.cget("background")
triad=Label(frame_chord,text='triad',bg='white',font=80)
triad.place(x=750,y=45)
######################CHORD MUTE
def chordmute():
    mixer.Channel(100).stop()
    mixer.Channel(101).stop()
    mixer.Channel(102).stop()
    mixer.Channel(103).stop()
####################### reset flash
def resetflash():
    def flashb1(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Escape>", flashb1)
    def flashb2(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-F8>", flashb2)
    def flashb3(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-`>", flashb3)
    def flashb4(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-1>", flashb4)
    def flashb5(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-2>", flashb5)
    def flashb6(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-3>", flashb6)
    def flashb7(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-4>", flashb7)
    def flashb8(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-5>", flashb8)
    def flashb9(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-6>", flashb9)
    def flashb10(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-7>", flashb10)
    def flashb11(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-8>", flashb11)
    def flashb12(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-9>", flashb12)
    def flashb13(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-0>", flashb13)
    def flashb14(event):
       scale_label.config(bg = orig_color)
    root.bind("-", flashb14)
    def flashb15(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-=>", flashb15)
    def flashb16(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-BackSpace>", flashb16)
    def flashb17(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Insert>", flashb17)
    def flashb18(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Home>", flashb18)
    def flashb19(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Prior>", flashb19)
    def flashb20(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-q>", flashb20)
    def flashb21(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-w>", flashb21)
    def flashb22(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-e>", flashb22)
    def flashb23(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-r>", flashb23)
    def flashb24(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-t>", flashb24)
    def flashb25(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-y>", flashb25)
    def flashb26(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-u>", flashb26)
    def flashb27(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-i>", flashb27)
    def flashb28(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-o>", flashb28)
    def flashb29(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-p>", flashb29)
    def flashb30(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-[>", flashb30)
    def flashb31(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-]>", flashb31)
    def flashb32(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-\>", flashb32)
    def flashb33(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Delete>", flashb33)
    def flashb34(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-End>", flashb34)
    def flashb35(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Next>", flashb35)
    def flashb36(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-a>", flashb36)
    def flashb37(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-s>", flashb37)
    def flashb38(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-d>", flashb38)
    def flashb39(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-f>", flashb39)
    def flashb40(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-g>", flashb40)
    def flashb41(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-h>", flashb41)
    def flashb42(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-j>", flashb42)
    def flashb43(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-k>", flashb43)
    def flashb44(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-l>", flashb44)
    def flashb45(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-;>", flashb45)
    def flashb46(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-'>", flashb46)
    def flashb47(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Return>", flashb47)
    def flashb48(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-z>", flashb48)
    def flashb49(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-x>", flashb49)
    def flashb50(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-c>", flashb50)
    def flashb51(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-v>", flashb51)
    def flashb52(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-b>", flashb52)
    def flashb53(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-n>", flashb53)
    def flashb54(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-m>", flashb54)
    def flashb55(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-,>", flashb55)
    def flashb56(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-.>", flashb56)
    def flashb57(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-/>", flashb57)
    def flashb58(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Left>", flashb58)
    def flashb59(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Down>", flashb59)
    def flashb60(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Right>", flashb60)
    def flashb61(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-I>", flashb61)
    def flashb62(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-O>", flashb62)
    def flashb63(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-P>", flashb63)
    def flashb64(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-{>", flashb64)
    def flashb65(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-}>", flashb65)
    def flashb66(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-|>", flashb66)
    def flashb67(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-A>", flashb67)
    def flashb68(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-S>", flashb68)
    def flashb69(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-D>", flashb69)
    def flashb70(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-F>", flashb70)
    def flashb71(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-G>", flashb71)
    def flashb72(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-H>", flashb72)
    def flashb73(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-J>", flashb73)
    def flashb74(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-K>", flashb74)
    def flashb75(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-L>", flashb75)
    def flashb76(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-:>", flashb76)
    def flashb77(event):
       scale_label.config(bg = orig_color)
    root.bind('<KeyPress-">', flashb77)
    def flashb78(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-Z>", flashb78)
    def flashb79(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-X>", flashb79)
    def flashb80(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-C>", flashb80)
    def flashb81(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-V>", flashb81)
    def flashb82(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-B>", flashb82)
    def flashb83(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-N>", flashb83)
    def flashb84(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-M>", flashb84)
    def flashb85(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-<>", flashb85)
    def flashb86(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress->>", flashb86)
    def flashb87(event):
       scale_label.config(bg = orig_color)
    root.bind("<KeyPress-?>", flashb87)


##################### reset piano
def resetpiano():
    b1.configure(background='white')
    b2.configure(background='black',foreground='white')
    b3.configure(background='white')
    b4.configure(background='black',foreground='white')
    b5.configure(background='white')
    b6.configure(background='white')
    b7.configure(background='black',foreground='white')
    b8.configure(background='white')
    b9.configure(background='black',foreground='white')
    b10.configure(background='white')
    b11.configure(background='black',foreground='white')
    b12.configure(background='white')
    b13.configure(background='white')
    b14.configure(background='black',foreground='white')
    b15.configure(background='white')
    b16.configure(background='black',foreground='white')
    b17.configure(background='white')
    b18.configure(background='white')
    b19.configure(background='black',foreground='white')
    b20.configure(background='white')
    b21.configure(background='black',foreground='white')
    b22.configure(background='white')
    b23.configure(background='black',foreground='white')
    b24.configure(background='white')
    b25.configure(background='white')
    b26.configure(background='black',foreground='white')
    b27.configure(background='white')
    b28.configure(background='black',foreground='white')
    b29.configure(background='white')
    b30.configure(background='white')
    b31.configure(background='black',foreground='white')
    b32.configure(background='white')
    b33.configure(background='black',foreground='white')
    b34.configure(background='white')
    b35.configure(background='black',foreground='white')
    b36.configure(background='white')
    b37.configure(background='white')
    b38.configure(background='black',foreground='white')
    b39.configure(background='white')
    b40.configure(background='black',foreground='white')
    b41.configure(background='white')
    b42.configure(background='white')
    b43.configure(background='black',foreground='white')
    b44.configure(background='white')
    b45.configure(background='black',foreground='white')
    b46.configure(background='white')
    b47.configure(background='black',foreground='white')
    b48.configure(background='white')
    b49.configure(background='white')
    b50.configure(background='black',foreground='white')
    b51.configure(background='white')
    b52.configure(background='black',foreground='white')
    b53.configure(background='white')
    b54.configure(background='white')
    b55.configure(background='black',foreground='white')
    b56.configure(background='white')
    b57.configure(background='black',foreground='white')
    b58.configure(background='white')
    b59.configure(background='black',foreground='white')
    b60.configure(background='white')
    b61.configure(background='white')
###################setting number of channels in mixer
mixer.set_num_channels(1000)
############################stopchannels
def stopchannels():
    mixer.Channel(0).stop()
    mixer.Channel(1).stop()
    mixer.Channel(2).stop()
    mixer.Channel(3).stop()
    mixer.Channel(4).stop()
    mixer.Channel(5).stop()
    mixer.Channel(6).stop()
    mixer.Channel(7).stop()
    mixer.Channel(8).stop()
    mixer.Channel(9).stop()
    mixer.Channel(10).stop()
    mixer.Channel(11).stop()
    mixer.Channel(12).stop()
    mixer.Channel(13).stop()
    mixer.Channel(14).stop()
    mixer.Channel(15).stop()
    mixer.Channel(16).stop()
    mixer.Channel(17).stop()
    mixer.Channel(18).stop()
    mixer.Channel(19).stop()
    mixer.Channel(20).stop()
    mixer.Channel(21).stop()
    mixer.Channel(22).stop()
    mixer.Channel(23).stop()
    mixer.Channel(24).stop()
    mixer.Channel(25).stop()
    mixer.Channel(26).stop()
    mixer.Channel(27).stop()
    mixer.Channel(28).stop()
    mixer.Channel(29).stop()
    mixer.Channel(30).stop()
    mixer.Channel(31).stop()
    mixer.Channel(32).stop()
    mixer.Channel(33).stop()
    mixer.Channel(34).stop()
    mixer.Channel(35).stop()
    mixer.Channel(36).stop()
    mixer.Channel(37).stop()
    mixer.Channel(38).stop()
    mixer.Channel(39).stop()
    mixer.Channel(40).stop()
    mixer.Channel(41).stop()
    mixer.Channel(42).stop()
    mixer.Channel(43).stop()
    mixer.Channel(44).stop()
    mixer.Channel(45).stop()
    mixer.Channel(46).stop()
    mixer.Channel(47).stop()
    mixer.Channel(48).stop()
    mixer.Channel(49).stop()
    mixer.Channel(50).stop()
    mixer.Channel(51).stop()
    mixer.Channel(52).stop()
    mixer.Channel(53).stop()
    mixer.Channel(54).stop()
    mixer.Channel(55).stop()
    mixer.Channel(56).stop()
    mixer.Channel(57).stop()
    mixer.Channel(58).stop()
    mixer.Channel(59).stop()
    mixer.Channel(60).stop()
    mixer.Channel(61).stop()

########################################default keyboard
def defaultkeyboard():
    resetpiano()
    resetflash()
    def flashb1(event):
       b1.config(bg = "green")
       root.after(175, lambda: b1.config(bg = "white"))
       g1()
    root.bind("<KeyPress-Escape>", flashb1)
    def flashb2(event):
       b2.config(bg = "green")
       root.after(175, lambda: b2.config(bg = "black",fg="white"))
       g2()
    root.bind("<KeyPress-F1>", flashb2)
    def flashb3(event):
       b3.config(bg = "green")
       root.after(175, lambda: b3.config(bg = "white"))
       g3()
    root.bind("<KeyPress-F2>", flashb3)
    def flashb4(event):
       b4.config(bg = "green")
       root.after(175, lambda: b4.config(bg = "black",fg="white"))
       g4()
    root.bind("<KeyPress-F3>", flashb4)
    def flashb5(event):
       b5.config(bg = "green")
       root.after(175, lambda: b5.config(bg = "white"))
       g5()
    root.bind("<KeyPress-F4>", flashb5)
    def flashb6(event):
       b6.config(bg = "green")
       root.after(175, lambda: b6.config(bg = "white"))
       g6()
    root.bind("<KeyPress-F5>", flashb6)
    def flashb7(event):
       b7.config(bg = "green")
       root.after(175, lambda: b7.config(bg = "black",fg="white"))
       g7()
    root.bind("<KeyPress-F6>", flashb7)
    def flashb8(event):
       b8.config(bg = "green")
       root.after(175, lambda: b8.config(bg = "white"))
       g8()
    root.bind("<KeyPress-F7>", flashb8)
    def flashb9(event):
       b9.config(bg = "green")
       root.after(175, lambda: b9.config(bg = "black",fg="white"))
       g9()
    root.bind("<KeyPress-F8>", flashb9)
    def flashb10(event):
       b10.config(bg = "green")
       root.after(175, lambda: b10.config(bg = "white"))
       g10()
    root.bind("<KeyPress-`>", flashb10)
    def flashb11(event):
       b11.config(bg = "green")
       root.after(175, lambda: b11.config(bg = "black",fg="white"))
       g11()
    root.bind("<KeyPress-1>", flashb11)
    def flashb12(event):
       b12.config(bg = "green")
       root.after(175, lambda: b12.config(bg = "white"))
       g12()
    root.bind("<KeyPress-2>", flashb12)
    def flashb13(event):
       b13.config(bg = "green")
       root.after(175, lambda: b13.config(bg = "white"))
       g13()
    root.bind("<KeyPress-3>", flashb13)
    def flashb14(event):
       b14.config(bg = "green")
       root.after(175, lambda: b14.config(bg = "black",fg="white"))
       g14()
    root.bind("<KeyPress-4>", flashb14)
    def flashb15(event):
       b15.config(bg = "green")
       root.after(175, lambda: b15.config(bg = "white"))
       g15()
    root.bind("<KeyPress-5>", flashb15)
    def flashb16(event):
       b16.config(bg = "green")
       root.after(175, lambda: b16.config(bg = "black",fg="white"))
       g16()
    root.bind("<KeyPress-6>", flashb16)
    def flashb17(event):
       b17.config(bg = "green")
       root.after(175, lambda: b17.config(bg = "white"))
       g17()
    root.bind("<KeyPress-7>", flashb17)
    def flashb18(event):
       b18.config(bg = "green")
       root.after(175, lambda: b18.config(bg = "white"))
       g18()
    root.bind("<KeyPress-8>", flashb18)
    def flashb19(event):
       b19.config(bg = "green")
       root.after(175, lambda: b19.config(bg = "black",fg="white"))
       g19()
    root.bind("<KeyPress-9>", flashb19)
    def flashb20(event):
       b20.config(bg = "green")
       root.after(175, lambda: b20.config(bg = "white"))
       g20()
    root.bind("<KeyPress-0>", flashb20)
    def flashb21(event):
       b21.config(bg = "green")
       root.after(175, lambda: b21.config(bg = "black",fg="white"))
       g21()
    root.bind("-", flashb21)
    def flashb22(event):
       b22.config(bg = "green")
       root.after(175, lambda: b22.config(bg = "white"))
       g22()
    root.bind("<KeyPress-=>", flashb22)
    def flashb23(event):
       b23.config(bg = "green")
       root.after(175, lambda: b23.config(bg = "black",fg="white"))
       g23()
    root.bind("<KeyPress-BackSpace>", flashb23)
    def flashb24(event):
       b24.config(bg = "green")
       root.after(175, lambda: b24.config(bg = "white"))
       g24()
    root.bind("<KeyPress-Insert>", flashb24)
    def flashb25(event):
       b25.config(bg = "green")
       root.after(175, lambda: b25.config(bg = "white"))
       g25()
    root.bind("<KeyPress-Home>", flashb25)
    def flashb26(event):
       b26.config(bg = "green")
       root.after(175, lambda: b26.config(bg = "black",fg="white"))
       g26()
    root.bind("<KeyPress-Prior>", flashb26)
    def flashb27(event):
       b27.config(bg = "green")
       root.after(175, lambda: b27.config(bg = "white"))
       g27()
    root.bind("<KeyPress-q>", flashb27)
    def flashb28(event):
       b28.config(bg = "green")
       root.after(175, lambda: b28.config(bg = "black",fg="white"))
       g28()
    root.bind("<KeyPress-w>", flashb28)
    def flashb29(event):
       b29.config(bg = "green")
       root.after(175, lambda: b29.config(bg = "white"))
       g29()
    root.bind("<KeyPress-e>", flashb29)
    def flashb30(event):
       b30.config(bg = "green")
       root.after(175, lambda: b30.config(bg = "white"))
       g30()
    root.bind("<KeyPress-r>", flashb30)
    def flashb31(event):
       b31.config(bg = "green")
       root.after(175, lambda: b31.config(bg = "black",fg="white"))
       g31()
    root.bind("<KeyPress-t>", flashb31)
    def flashb32(event):
       b32.config(bg = "green")
       root.after(175, lambda: b32.config(bg = "white"))
       g32()
    root.bind("<KeyPress-y>", flashb32)
    def flashb33(event):
       b33.config(bg = "green")
       root.after(175, lambda: b33.config(bg = "black",fg="white"))
       g33()
    root.bind("<KeyPress-u>", flashb33)
    def flashb34(event):
       b34.config(bg = "green")
       root.after(175, lambda: b34.config(bg = "white"))
       g34()
    root.bind("<KeyPress-i>", flashb34)
    def flashb35(event):
       b35.config(bg = "green")
       root.after(175, lambda: b35.config(bg = "black",fg="white"))
       g35()
    root.bind("<KeyPress-o>", flashb35)
    def flashb36(event):
       b36.config(bg = "green")
       root.after(175, lambda: b36.config(bg = "white"))
       g36()
    root.bind("<KeyPress-p>", flashb36)
    def flashb37(event):
       b37.config(bg = "green")
       root.after(175, lambda: b37.config(bg = "white"))
       g37()
    root.bind("<KeyPress-[>", flashb37)
    def flashb38(event):
       b38.config(bg = "green")
       root.after(175, lambda: b38.config(bg = "black",fg="white"))
       g38()
    root.bind("<KeyPress-]>", flashb38)
    def flashb39(event):
       b39.config(bg = "green")
       root.after(175, lambda: b39.config(bg = "white"))
       g39()
    root.bind("<KeyPress-\>", flashb39)
    def flashb40(event):
       b40.config(bg = "green")
       root.after(175, lambda: b40.config(bg = "black",fg="white"))
       g40()
    root.bind("<KeyPress-Delete>", flashb40)
    def flashb41(event):
       b41.config(bg = "green")
       root.after(175, lambda: b41.config(bg = "white"))
       g41()
    root.bind("<KeyPress-End>", flashb41)
    def flashb42(event):
       b42.config(bg = "green")
       root.after(175, lambda: b42.config(bg = "white"))
       g42()
    root.bind("<KeyPress-Next>", flashb42)
    def flashb43(event):
       b43.config(bg = "green")
       root.after(175, lambda: b43.config(bg = "black",fg="white"))
       g43()
    root.bind("<KeyPress-a>", flashb43)
    def flashb44(event):
       b44.config(bg = "green")
       root.after(175, lambda: b44.config(bg = "white"))
       g44()
    root.bind("<KeyPress-s>", flashb44)
    def flashb45(event):
       b45.config(bg = "green")
       root.after(175, lambda: b45.config(bg = "black",fg="white"))
       g45()
    root.bind("<KeyPress-d>", flashb45)
    def flashb46(event):
       b46.config(bg = "green")
       root.after(175, lambda: b46.config(bg = "white"))
       g46()
    root.bind("<KeyPress-f>", flashb46)
    def flashb47(event):
       b47.config(bg = "green")
       root.after(175, lambda: b47.config(bg = "black",fg="white"))
       g47()
    root.bind("<KeyPress-g>", flashb47)
    def flashb48(event):
       b48.config(bg = "green")
       root.after(175, lambda: b48.config(bg = "white"))
       g48()
    root.bind("<KeyPress-h>", flashb48)
    def flashb49(event):
       b49.config(bg = "green")
       root.after(175, lambda: b49.config(bg = "white"))
       g49()
    root.bind("<KeyPress-j>", flashb49)
    def flashb50(event):
       b50.config(bg = "green")
       root.after(175, lambda: b50.config(bg = "black",fg="white"))
       g50()
    root.bind("<KeyPress-k>", flashb50)
    def flashb51(event):
       b51.config(bg = "green")
       root.after(175, lambda: b51.config(bg = "white"))
       g51()
    root.bind("<KeyPress-l>", flashb51)
    def flashb52(event):
       b52.config(bg = "green")
       root.after(175, lambda: b52.config(bg = "black",fg="white"))
       g52()
    root.bind("<KeyPress-;>", flashb52)
    def flashb53(event):
       b53.config(bg = "green")
       root.after(175, lambda: b53.config(bg = "white"))
       g53()
    root.bind("<KeyPress-'>", flashb53)
    def flashb54(event):
       b54.config(bg = "green")
       root.after(175, lambda: b54.config(bg = "white"))
       g54()
    root.bind("<KeyPress-Return>", flashb54)
    def flashb55(event):
       b55.config(bg = "green")
       root.after(175, lambda: b55.config(bg = "black",fg="white"))
       g55()
    root.bind("<KeyPress-z>", flashb55)
    def flashb56(event):
       b56.config(bg = "green")
       root.after(175, lambda: b56.config(bg = "white"))
       g56()
    root.bind("<KeyPress-x>", flashb56)
    def flashb57(event):
       b57.config(bg = "green")
       root.after(175, lambda: b57.config(bg = "black",fg="white"))
       g57()
    root.bind("<KeyPress-c>", flashb57)
    def flashb58(event):
       b58.config(bg = "green")
       root.after(175, lambda: b58.config(bg = "white"))
       g58()
    root.bind("<KeyPress-v>", flashb58)
    def flashb59(event):
       b59.config(bg = "green")
       root.after(175, lambda: b59.config(bg = "black",fg="white"))
       g59()
    root.bind("<KeyPress-b>", flashb59)
    def flashb60(event):
       b60.config(bg = "green")
       root.after(175, lambda: b60.config(bg = "white"))
       g60()
    root.bind("<KeyPress-n>", flashb60)
    def flashb61(event):
       b61.config(bg = "green")
       root.after(175, lambda: b61.config(bg = "white"))
       g61()
    root.bind("<KeyPress-m>", flashb61)
     

#######################RESET CHORDS
def resetchords():
    c1.place_forget()
    c2.place_forget()
    c3.place_forget()
    c4.place_forget()
    c5.place_forget()
    c6.place_forget()
    c7.place_forget()
    c8.place_forget()
    c9.place_forget()
    c10.place_forget()
    c11.place_forget()
    c12.place_forget()
    c13.place_forget()
    c14.place_forget()
    c15.place_forget()
    c16.place_forget()
    c17.place_forget()
    c18.place_forget()
    c19.place_forget()
    c20.place_forget()
    c21.place_forget()
    c22.place_forget()
    c23.place_forget()
    c24.place_forget()
    c25.place_forget()
    c26.place_forget()
    c27.place_forget()
    c28.place_forget()
    c29.place_forget()
    c30.place_forget()
    c31.place_forget()
    c32.place_forget()
    c33.place_forget()
    c34.place_forget()
    c35.place_forget()
    c36.place_forget()
    c37.place_forget()
    c38.place_forget()
    c39.place_forget()
    c40.place_forget()
    c41.place_forget()
    c42.place_forget()
    c43.place_forget()
    c44.place_forget()
    c45.place_forget()
    c46.place_forget()
    c47.place_forget()
    c48.place_forget()
    c49.place_forget()
    c50.place_forget()
    c51.place_forget()
    c52.place_forget()
    c53.place_forget()
    c54.place_forget()
    c55.place_forget()
    c56.place_forget()
    c57.place_forget()
    c58.place_forget()
    c59.place_forget()
    c60.place_forget()
    c61.place_forget()
    c62.place_forget()
    c63.place_forget()
    c64.place_forget()
    c65.place_forget()
    c66.place_forget()
    c67.place_forget()
    c68.place_forget()
    c69.place_forget()
    c70.place_forget()
    c71.place_forget()
    c72.place_forget()
    c73.place_forget()
    c74.place_forget()
    c75.place_forget()
    c76.place_forget()
    c77.place_forget()
    c78.place_forget()
    c79.place_forget()
    c80.place_forget()
    c81.place_forget()
    c82.place_forget()
    c83.place_forget()
    c84.place_forget()
##############default scale buton############
default_scale=Button(frame_major,text='All notes mode',command=defaultkeyboard)
default_scale.place(x=1200,y=45,height=50,width=150)
###############################################
def chordC():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    triad.configure(text="C-E-G")
    b1.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
def chordCsharp():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    triad.configure(text="C#-F-G#")
    b2.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
def chordD():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    triad.configure(text="D-F#-A")
    b3.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
def chordDsharp():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    triad.configure(text="D#-G-A#")
    b4.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
def chordE():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="E-G#-B")
    b5.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordF():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="F-A-C")
    b6.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordFsharp():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="F#-A#-C#")
    b7.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordG():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="G-B-D")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordGsharp():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="G#-C-D#")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordA():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="A-C#-E")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordAsharp():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="A#-D-F")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordB():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P19.wav"))
    triad.configure(text="B-D#-F#")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")

def chordCminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    triad.configure(text="C-D#-G")
    b1.configure(background="#ff12eb")
    b4.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
def chordCsharpminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    triad.configure(text="C#-E-G#")
    b2.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
def chordDminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    triad.configure(text="D-F-A")
    b3.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
def chordDsharpminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    triad.configure(text="D#-F#-A#")
    b4.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
def chordEminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="E-G-B")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordFminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="F-G#-C")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordFsharpminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="F#-A-C#")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordGminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="G-A#-D")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordGsharpminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="G#-B-D#")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordAminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="A-C-E")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordAsharpminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="A#-C#-F")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordBminor():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P19.wav"))
    triad.configure(text="B-D-F#")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")

def chordCdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P7.wav"))
    triad.configure(text="C-D#-F#")
    b1.configure(background="#ff12eb")
    b4.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
def chordCsharpdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    triad.configure(text="C#-E-G")
    b2.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
def chordDdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    triad.configure(text="D-F-G#")
    b3.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
def chordDsharpdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    triad.configure(text="D#-F#-A")
    b4.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
def chordEdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    triad.configure(text="E-G-A#")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
def chordFdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="F-G#-B")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordFsharpdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="F#-A-C")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordGdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="G-A#-C#")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordGsharpdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="G#-B-D")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordAdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="A-C-D#")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordAsharpdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="A#-C#-E")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordBdiminished():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="B-D-F")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordCmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="C-E-G-B")
    b1.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordCsharpmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="C#-F-G#-C")
    b2.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordDmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="D-F#-A-C#")
    b3.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordDsharpmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="D#-G-A#-D")
    b4.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordEmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="E-G#-B-D#")
    b5.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordFmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="F-A-C-E")
    b6.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordFsharpmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="F#-A#-C#-F")
    b7.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordGmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P19.wav"))
    triad.configure(text="G-B-D-F#")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
def chordGsharpmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P20.wav"))
    triad.configure(text="G#-C-D#-G")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b20.configure(background="#ff12eb")
def chordAmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P21.wav"))
    triad.configure(text="A-C#-E-G#")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
    b21.configure(background="#ff12eb")
def chordAsharpmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P22.wav"))
    triad.configure(text="A#-D-F-A")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
    b22.configure(background="#ff12eb")
def chordBmajor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P19.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P23.wav"))
    triad.configure(text="B-D#-F#-A#")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
    b23.configure(background="#ff12eb")

def chordCminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P11.wav"))
    triad.configure(text="C-D#-G-A#")
    b1.configure(background="#ff12eb")
    b4.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
def chordCsharpminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="C#-E-G#-B")
    b2.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordDminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="D-F-A-C")
    b3.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordDsharpminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="D#-F#-A#-C#")
    b4.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordEminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="E-G-B-D")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordFminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="F-G#-C-D#")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordFsharpminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="F#-A-C#-E")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordGminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="G-A#-D-F")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordGsharpminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P19.wav"))
    triad.configure(text="G#-B-D#-F#")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
def chordAminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P20.wav"))
    triad.configure(text="A-C-E-G")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
    b20.configure(background="#ff12eb")
def chordAsharpminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P21.wav"))
    triad.configure(text="A#-C#-F-G#")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
    b21.configure(background="#ff12eb")
def chordBminor7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P19.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P22.wav"))
    triad.configure(text="B-D-F#-A")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
    b22.configure(background="#ff12eb")


def chordCdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P11.wav"))
    triad.configure(text="C-E-G-A#")
    b1.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
def chordCsharpdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="C#-F-G#-B")
    b2.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordDdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="D-F#-A-C")
    b3.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordDsharpdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="D#-G-A#-C#")
    b4.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordEdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="E-G#-B-D")
    b5.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordFdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="F-A-C-D#")
    b6.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordFsharpdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="F#-A#-C#-E")
    b7.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordGdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="G-B-D-F")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordGsharpdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P19.wav"))
    triad.configure(text="G#-C-D#-F#")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
def chordAdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P20.wav"))
    triad.configure(text="A-C#-E-G")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
    b20.configure(background="#ff12eb")
def chordAsharpdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P21.wav"))
    triad.configure(text="A#-D-F-G#")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
    b21.configure(background="#ff12eb")
def chordBdominant7():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P19.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P22.wav"))
    triad.configure(text="B-D#-F#-A")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
    b22.configure(background="#ff12eb")
def chordCminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P1.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P11.wav"))
    triad.configure(text="C-D#-F#-A#")
    b1.configure(background="#ff12eb")
    b4.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
def chordCsharpminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P2.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P12.wav"))
    triad.configure(text="C#-E-G-B")
    b2.configure(background="#ff12eb")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
def chordDminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P3.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P13.wav"))
    triad.configure(text="D-F-G#-C")
    b3.configure(background="#ff12eb")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
def chordDsharpminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P4.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P14.wav"))
    triad.configure(text="D#-F#-A-C#")
    b4.configure(background="#ff12eb")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
def chordEminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P5.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P15.wav"))
    triad.configure(text="E-G-A#-D")
    b5.configure(background="#ff12eb")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
def chordFminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P6.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P16.wav"))
    triad.configure(text="F-G#-B-D#")
    b6.configure(background="#ff12eb")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
def chordFsharpminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P7.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P17.wav"))
    triad.configure(text="F#-A-C-E")
    b7.configure(background="#ff12eb")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
def chordGminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P8.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P18.wav"))
    triad.configure(text="G-A#-C#-F")
    b8.configure(background="#ff12eb")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
def chordGsharpminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P9.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P19.wav"))
    triad.configure(text="G#-B-D-F#")
    b9.configure(background="#ff12eb")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b19.configure(background="#ff12eb")
def chordAminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P10.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P13.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P16.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P20.wav"))
    triad.configure(text="A-C-D#-G")
    b10.configure(background="#ff12eb")
    b13.configure(background="#ff12eb")
    b16.configure(background="#ff12eb")
    b20.configure(background="#ff12eb")
def chordAsharpminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P11.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P14.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P17.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P21.wav"))
    triad.configure(text="A#-C#-E-G#")
    b11.configure(background="#ff12eb")
    b14.configure(background="#ff12eb")
    b17.configure(background="#ff12eb")
    b21.configure(background="#ff12eb")
def chordBminor7flat5():
    chordmute()
    mixer.Channel(100).play(mixer.Sound("Audio/P12.wav"))
    mixer.Channel(101).play(mixer.Sound("Audio/P15.wav"))
    mixer.Channel(102).play(mixer.Sound("Audio/P18.wav"))
    mixer.Channel(103).play(mixer.Sound("Audio/P22.wav"))
    triad.configure(text="B-D-F-A")
    b12.configure(background="#ff12eb")
    b15.configure(background="#ff12eb")
    b18.configure(background="#ff12eb")
    b22.configure(background="#ff12eb")


#############flag variable##############################
flag=0  
#################################Chord Scale Button Function##########################################
def c1f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordC() 
def c2f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharp()
def c3f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordD()
def c4f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharp()
def c5f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordE()
def c6f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordF()
def c7f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharp()
def c8f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordG()
def c9f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharp()
def c10f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordA()
def c11f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharp()
def c12f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordB()
def c13f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCminor()
def c14f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpminor()
def c15f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDminor()
def c16f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpminor()
def c17f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEminor()
def c18f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFminor()
def c19f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpminor()
def c20f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGminor()
def c21f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpminor()
def c22f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAminor()
def c23f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpminor()
def c24f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBminor()
def c25f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCdiminished()
def c26f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpdiminished()
def c27f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDdiminished()
def c28f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpdiminished()
def c29f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEdiminished()
def c30f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFdiminished()
def c31f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpdiminished()
def c32f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGdiminished()
def c33f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpdiminished()
def c34f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAdiminished()
def c35f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpdiminished()
def c36f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBdiminished()
def c37f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCmajor7()
def c38f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpmajor7()
def c39f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDmajor7()
def c40f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpmajor7()
def c41f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEmajor7()
def c42f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFmajor7()
def c43f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpmajor7()
def c44f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGmajor7()
def c45f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpmajor7()
def c46f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAmajor7()
def c47f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpmajor7()
def c48f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBmajor7()
def c49f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCminor7()
def c50f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpminor7()
def c51f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDminor7()
def c52f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpminor7()
def c53f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEminor7()
def c54f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFminor7()
def c55f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpminor7()
def c56f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGminor7()
def c57f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpminor7()
def c58f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAminor7()
def c59f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpminor7()
def c60f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBminor7()
def c61f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCdominant7()
def c62f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpdominant7()
def c63f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDdominant7()
def c64f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpdominant7()
def c65f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEdominant7()
def c66f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFdominant7()
def c67f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpdominant7()
def c68f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGdominant7()
def c69f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpdominant7()
def c70f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAdominant7()
def c71f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpdominant7()
def c72f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBdominant7()
def c73f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCminor7flat5()
def c74f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpminor7flat5()
def c75f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDminor7flat5()
def c76f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpminor7flat5()
def c77f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEminor7flat5()
def c78f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFminor7flat5()
def c79f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpminor7flat5()
def c80f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGminor7flat5()
def c81f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpminor7flat5()
def c82f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAminor7flat5()
def c83f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpminor7flat5()
def c84f():
    resetpiano()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBminor7flat5()
#################################Chord Scale Button ##########################################
c1=Button(frame_chord,text='C',command=c1f)
c2=Button(frame_chord,text='C#',command=c2f)
c3=Button(frame_chord,text='D',command=c3f)
c4=Button(frame_chord,text='D#',command=c4f)
c5=Button(frame_chord,text='E',command=c5f)
c6=Button(frame_chord,text='F',command=c6f)
c7=Button(frame_chord,text='F#',command=c7f)
c8=Button(frame_chord,text='G',command=c8f)
c9=Button(frame_chord,text='G#',command=c9f)
c10=Button(frame_chord,text='A',command=c10f)
c11=Button(frame_chord,text='A#',command=c11f)
c12=Button(frame_chord,text='B',command=c12f)
c13=Button(frame_chord,text='Cm',command=c13f)
c14=Button(frame_chord,text='C#m',command=c14f)
c15=Button(frame_chord,text='Dm',command=c15f)
c16=Button(frame_chord,text='D#m',command=c16f)
c17=Button(frame_chord,text='Em',command=c17f)
c18=Button(frame_chord,text='Fm',command=c18f)
c19=Button(frame_chord,text='F#m',command=c19f)
c20=Button(frame_chord,text='Gm',command=c20f)
c21=Button(frame_chord,text='G#m',command=c21f)
c22=Button(frame_chord,text='Am',command=c22f)
c23=Button(frame_chord,text='A#m',command=c23f)
c24=Button(frame_chord,text='Bm',command=c24f)
c25=Button(frame_chord,text='Cdim',command=c25f)
c26=Button(frame_chord,text='C#dim',command=c26f)
c27=Button(frame_chord,text='Ddim',command=c27f)
c28=Button(frame_chord,text='D#dim',command=c28f)
c29=Button(frame_chord,text='Edim',command=c29f)
c30=Button(frame_chord,text='Fdim',command=c30f)
c31=Button(frame_chord,text='F#dim',command=c31f)
c32=Button(frame_chord,text='Gdim',command=c32f)
c33=Button(frame_chord,text='G#dim',command=c33f)
c34=Button(frame_chord,text='Adim',command=c34f)
c35=Button(frame_chord,text='A#dim',command=c35f)
c36=Button(frame_chord,text='Bdim',command=c36f)
c37=Button(frame_chord,text='Cmaj7',command=c37f)
c38=Button(frame_chord,text='C#maj7',command=c38f)
c39=Button(frame_chord,text='Dmaj7',command=c39f)
c40=Button(frame_chord,text='D#maj7',command=c40f)
c41=Button(frame_chord,text='Emaj7',command=c41f)
c42=Button(frame_chord,text='Fmaj7',command=c42f)
c43=Button(frame_chord,text='F#maj7',command=c43f)
c44=Button(frame_chord,text='Gmaj7',command=c44f)
c45=Button(frame_chord,text='G#maj7',command=c45f)
c46=Button(frame_chord,text='Amaj7',command=c46f)
c47=Button(frame_chord,text='A#maj7',command=c47f)
c48=Button(frame_chord,text='Bmaj7',command=c48f)
c49=Button(frame_chord,text='Cmin7',command=c49f)
c50=Button(frame_chord,text='C#min7',command=c50f)
c51=Button(frame_chord,text='Dmin7',command=c51f)
c52=Button(frame_chord,text='D#min7',command=c52f)
c53=Button(frame_chord,text='Emin7',command=c53f)
c54=Button(frame_chord,text='Fmin7',command=c54f)
c55=Button(frame_chord,text='F#min7',command=c55f)
c56=Button(frame_chord,text='Gmin7',command=c56f)
c57=Button(frame_chord,text='G#min7',command=c57f)
c58=Button(frame_chord,text='Amin7',command=c58f)
c59=Button(frame_chord,text='A#min7',command=c59f)
c60=Button(frame_chord,text='Bmin7',command=c60f) 
c61=Button(frame_chord,text='Cdom7',command=c61f)
c62=Button(frame_chord,text='C#dom7',command=c62f)
c63=Button(frame_chord,text='Ddom7',command=c63f)
c64=Button(frame_chord,text='D#dom7',command=c64f)
c65=Button(frame_chord,text='Edom7',command=c65f)
c66=Button(frame_chord,text='Fdom7',command=c66f)
c67=Button(frame_chord,text='F#dom7',command=c67f)
c68=Button(frame_chord,text='Gdom7',command=c68f)
c69=Button(frame_chord,text='G#dom7',command=c69f)
c70=Button(frame_chord,text='Adom7',command=c70f)
c71=Button(frame_chord,text='A#dom7',command=c71f)
c72=Button(frame_chord,text='Bdom7',command=c72f)
c73=Button(frame_chord,text='Cmin7b5',command=c73f)
c74=Button(frame_chord,text='C#min7b5',command=c74f)
c75=Button(frame_chord,text='Dmin7b5',command=c75f)
c76=Button(frame_chord,text='D#min7b5',command=c76f)
c77=Button(frame_chord,text='Emin7b5',command=c77f)
c78=Button(frame_chord,text='Fmin7b5',command=c78f)
c79=Button(frame_chord,text='F#min7b5',command=c79f)
c80=Button(frame_chord,text='Gmin7b5',command=c80f)
c81=Button(frame_chord,text='G#min7b5',command=c81f)
c82=Button(frame_chord,text='Amin7b5',command=c82f)
c83=Button(frame_chord,text='A#min7b5',command=c83f)
c84=Button(frame_chord,text='Bmin7b5',command=c84f)
########################show scale
def showscale1():
    resetchords()
    resetpiano()
    global flag
    flag=1
    c_major_show()
    c1.config(bg='yellow')
    def flashb1(event):
       c1.config(bg = 'green')
       root.after(175, lambda: c1.config(bg = 'yellow'))
       c1f()
    root.bind('<KeyPress-F1>', flashb1)
    c1.place(x=0,y=30,height=30,width=80)
    c15.config(bg='yellow')
    def flashb2(event):
       c15.config(bg = 'green')
       root.after(175, lambda: c15.config(bg = 'yellow'))
       c15f()
    root.bind('<KeyPress-F2>', flashb2)
    c15.place(x=90,y=30,height=30,width=80)
    c17.config(bg='yellow')
    def flashb3(event):
       c17.config(bg = 'green')
       root.after(175, lambda: c17.config(bg = 'yellow'))
       c17f()
    root.bind('<KeyPress-F3>', flashb3)
    c17.place(x=180,y=30,height=30,width=80)
    c6.config(bg='yellow')
    def flashb4(event):
       c6.config(bg = 'green')
       root.after(175, lambda: c6.config(bg = 'yellow'))
       c6f()
    root.bind('<KeyPress-F4>', flashb4)
    c6.place(x=270,y=30,height=30,width=80)
    c8.config(bg='yellow')
    def flashb5(event):
       c8.config(bg = 'green')
       root.after(175, lambda: c8.config(bg = 'yellow'))
       c8f()
    root.bind('<KeyPress-F5>', flashb5)
    c8.place(x=360,y=30,height=30,width=80)
    c22.config(bg='yellow')
    def flashb6(event):
       c22.config(bg = 'green')
       root.after(175, lambda: c22.config(bg = 'yellow'))
       c22f()
    root.bind('<KeyPress-F6>', flashb6)
    c22.place(x=450,y=30,height=30,width=80)
    c36.config(bg='yellow')
    def flashb7(event):
       c36.config(bg = 'green')
       root.after(175, lambda: c36.config(bg = 'yellow'))
       c36f()
    root.bind('<KeyPress-F7>', flashb7)
    c36.place(x=560,y=30,height=30,width=80)
    c37.config(bg='yellow')
    def flashb8(event):
       c37.config(bg = 'green')
       root.after(175, lambda: c37.config(bg = 'yellow'))
       c37f()
    root.bind('<KeyPress-Q>', flashb8)
    c37.place(x=0,y=60,height=30,width=80)
    c51.config(bg='yellow')
    def flashb9(event):
       c51.config(bg = 'green')
       root.after(175, lambda: c51.config(bg = 'yellow'))
       c51f()
    root.bind('<KeyPress-W>', flashb9)
    c51.place(x=90,y=60,height=30,width=80)
    c53.config(bg='yellow')
    def flashb10(event):
       c53.config(bg = 'green')
       root.after(175, lambda: c53.config(bg = 'yellow'))
       c53f()
    root.bind('<KeyPress-E>', flashb10)
    c53.place(x=180,y=60,height=30,width=80)
    c42.config(bg='yellow')
    def flashb11(event):
       c42.config(bg = 'green')
       root.after(175, lambda: c42.config(bg = 'yellow'))
       c42f()
    root.bind('<KeyPress-R>', flashb11)
    c42.place(x=270,y=60,height=30,width=80)
    c68.config(bg='yellow')
    def flashb12(event):
       c68.config(bg = 'green')
       root.after(175, lambda: c68.config(bg = 'yellow'))
       c68f()
    root.bind('<KeyPress-T>', flashb12)
    c68.place(x=360,y=60,height=30,width=80)
    c58.config(bg='yellow')
    def flashb13(event):
       c58.config(bg = 'green')
       root.after(175, lambda: c58.config(bg = 'yellow'))
       c58f()
    root.bind('<KeyPress-Y>', flashb13)
    c58.place(x=450,y=60,height=30,width=80)
    c84.config(bg='yellow')
    def flashb14(event):
       c84.config(bg = 'green')
       root.after(175, lambda: c84.config(bg = 'yellow'))
       c84f()
    root.bind('<KeyPress-U>', flashb14)
    c84.place(x=560,y=60,height=30,width=80)
def showscale2():
    resetchords()
    resetpiano()
    global flag
    flag=2
    c_sharp_major_show()
    c2.config(bg='orange')
    def flashb1(event):
       c2.config(bg = 'green')
       root.after(175, lambda: c2.config(bg = 'orange'))
       c2f()
    root.bind('<KeyPress-F1>', flashb1)
    c2.place(x=0,y=30,height=30,width=80)
    c16.config(bg='orange')
    def flashb2(event):
       c16.config(bg = 'green')
       root.after(175, lambda: c16.config(bg = 'orange'))
       c16f()
    root.bind('<KeyPress-F2>', flashb2)
    c16.place(x=90,y=30,height=30,width=80)
    c18.config(bg='orange')
    def flashb3(event):
       c18.config(bg = 'green')
       root.after(175, lambda: c18.config(bg = 'orange'))
       c18f()
    root.bind('<KeyPress-F3>', flashb3)
    c18.place(x=180,y=30,height=30,width=80)
    c7.config(bg='orange')
    def flashb4(event):
       c7.config(bg = 'green')
       root.after(175, lambda: c7.config(bg = 'orange'))
       c7f()
    root.bind('<KeyPress-F4>', flashb4)
    c7.place(x=270,y=30,height=30,width=80)
    c9.config(bg='orange')
    def flashb5(event):
       c9.config(bg = 'green')
       root.after(175, lambda: c9.config(bg = 'orange'))
       c9f()
    root.bind('<KeyPress-F5>', flashb5)
    c9.place(x=360,y=30,height=30,width=80)
    c23.config(bg='orange')
    def flashb6(event):
       c23.config(bg = 'green')
       root.after(175, lambda: c23.config(bg = 'orange'))
       c23f()
    root.bind('<KeyPress-F6>', flashb6)
    c23.place(x=450,y=30,height=30,width=80)
    c25.config(bg='orange')
    def flashb7(event):
       c25.config(bg = 'green')
       root.after(175, lambda: c25.config(bg = 'orange'))
       c25f()
    root.bind('<KeyPress-F7>', flashb7)
    c25.place(x=560,y=30,height=30,width=80)
    c38.config(bg='orange')
    def flashb8(event):
       c38.config(bg = 'green')
       root.after(175, lambda: c38.config(bg = 'orange'))
       c38f()
    root.bind('<KeyPress-Q>', flashb8)
    c38.place(x=0,y=60,height=30,width=80)
    c52.config(bg='orange')
    def flashb9(event):
       c52.config(bg = 'green')
       root.after(175, lambda: c52.config(bg = 'orange'))
       c52f()
    root.bind('<KeyPress-W>', flashb9)
    c52.place(x=90,y=60,height=30,width=80)
    c54.config(bg='orange')
    def flashb10(event):
       c54.config(bg = 'green')
       root.after(175, lambda: c54.config(bg = 'orange'))
       c54f()
    root.bind('<KeyPress-E>', flashb10)
    c54.place(x=180,y=60,height=30,width=80)
    c43.config(bg='orange')
    def flashb11(event):
       c43.config(bg = 'green')
       root.after(175, lambda: c43.config(bg = 'orange'))
       c43f()
    root.bind('<KeyPress-R>', flashb11)
    c43.place(x=270,y=60,height=30,width=80)
    c69.config(bg='orange')
    def flashb12(event):
       c69.config(bg = 'green')
       root.after(175, lambda: c69.config(bg = 'orange'))
       c69f()
    root.bind('<KeyPress-T>', flashb12)
    c69.place(x=360,y=60,height=30,width=80)
    c59.config(bg='orange')
    def flashb13(event):
       c59.config(bg = 'green')
       root.after(175, lambda: c59.config(bg = 'orange'))
       c59f()
    root.bind('<KeyPress-Y>', flashb13)
    c59.place(x=450,y=60,height=30,width=80)
    c73.config(bg='orange')
    def flashb14(event):
       c73.config(bg = 'green')
       root.after(175, lambda: c73.config(bg = 'orange'))
       c73f()
    root.bind('<KeyPress-U>', flashb14)
    c73.place(x=560,y=60,height=30,width=80)
def showscale3():
    resetchords()
    resetpiano()
    global flag
    flag=3
    d_major_show()
    c3.config(bg='#41d95f')
    def flashb1(event):
       c3.config(bg = 'green')
       root.after(175, lambda: c3.config(bg = '#41d95f'))
       c3f()
    root.bind('<KeyPress-F1>', flashb1)
    c3.place(x=0,y=30,height=30,width=80)
    c17.config(bg='#41d95f')
    def flashb2(event):
       c17.config(bg = 'green')
       root.after(175, lambda: c17.config(bg = '#41d95f'))
       c17f()
    root.bind('<KeyPress-F2>', flashb2)
    c17.place(x=90,y=30,height=30,width=80)
    c19.config(bg='#41d95f')
    def flashb3(event):
       c19.config(bg = 'green')
       root.after(175, lambda: c19.config(bg = '#41d95f'))
       c19f()
    root.bind('<KeyPress-F3>', flashb3)
    c19.place(x=180,y=30,height=30,width=80)
    c8.config(bg='#41d95f')
    def flashb4(event):
       c8.config(bg = 'green')
       root.after(175, lambda: c8.config(bg = '#41d95f'))
       c8f()
    root.bind('<KeyPress-F4>', flashb4)
    c8.place(x=270,y=30,height=30,width=80)
    c10.config(bg='#41d95f')
    def flashb5(event):
       c10.config(bg = 'green')
       root.after(175, lambda: c10.config(bg = '#41d95f'))
       c10f()
    root.bind('<KeyPress-F5>', flashb5)
    c10.place(x=360,y=30,height=30,width=80)
    c24.config(bg='#41d95f')
    def flashb6(event):
       c24.config(bg = 'green')
       root.after(175, lambda: c24.config(bg = '#41d95f'))
       c24f()
    root.bind('<KeyPress-F6>', flashb6)
    c24.place(x=450,y=30,height=30,width=80)
    c26.config(bg='#41d95f')
    def flashb7(event):
       c26.config(bg = 'green')
       root.after(175, lambda: c26.config(bg = '#41d95f'))
       c26f()
    root.bind('<KeyPress-F7>', flashb7)
    c26.place(x=560,y=30,height=30,width=80)
    c39.config(bg='#41d95f')
    def flashb8(event):
       c39.config(bg = 'green')
       root.after(175, lambda: c39.config(bg = '#41d95f'))
       c39f()
    root.bind('<KeyPress-Q>', flashb8)
    c39.place(x=0,y=60,height=30,width=80)
    c53.config(bg='#41d95f')
    def flashb9(event):
       c53.config(bg = 'green')
       root.after(175, lambda: c53.config(bg = '#41d95f'))
       c53f()
    root.bind('<KeyPress-W>', flashb9)
    c53.place(x=90,y=60,height=30,width=80)
    c55.config(bg='#41d95f')
    def flashb10(event):
       c55.config(bg = 'green')
       root.after(175, lambda: c55.config(bg = '#41d95f'))
       c55f()
    root.bind('<KeyPress-E>', flashb10)
    c55.place(x=180,y=60,height=30,width=80)
    c44.config(bg='#41d95f')
    def flashb11(event):
       c44.config(bg = 'green')
       root.after(175, lambda: c44.config(bg = '#41d95f'))
       c44f()
    root.bind('<KeyPress-R>', flashb11)
    c44.place(x=270,y=60,height=30,width=80)
    c70.config(bg='#41d95f')
    def flashb12(event):
       c70.config(bg = 'green')
       root.after(175, lambda: c70.config(bg = '#41d95f'))
       c70f()
    root.bind('<KeyPress-T>', flashb12)
    c70.place(x=360,y=60,height=30,width=80)
    c60.config(bg='#41d95f')
    def flashb13(event):
       c60.config(bg = 'green')
       root.after(175, lambda: c60.config(bg = '#41d95f'))
       c60f()
    root.bind('<KeyPress-Y>', flashb13)
    c60.place(x=450,y=60,height=30,width=80)
    c74.config(bg='#41d95f')
    def flashb14(event):
       c74.config(bg = 'green')
       root.after(175, lambda: c74.config(bg = '#41d95f'))
       c74f()
    root.bind('<KeyPress-U>', flashb14)
    c74.place(x=560,y=60,height=30,width=80)
def showscale4():
    resetchords()
    resetpiano()
    global flag
    flag=4
    d_sharp_major_show()
    c4.config(bg='#6fedd0')
    def flashb1(event):
       c4.config(bg = 'green')
       root.after(175, lambda: c4.config(bg = '#6fedd0'))
       c4f()
    root.bind('<KeyPress-F1>', flashb1)
    c4.place(x=0,y=30,height=30,width=80)
    c18.config(bg='#6fedd0')
    def flashb2(event):
       c18.config(bg = 'green')
       root.after(175, lambda: c18.config(bg = '#6fedd0'))
       c18f()
    root.bind('<KeyPress-F2>', flashb2)
    c18.place(x=90,y=30,height=30,width=80)
    c20.config(bg='#6fedd0')
    def flashb3(event):
       c20.config(bg = 'green')
       root.after(175, lambda: c20.config(bg = '#6fedd0'))
       c20f()
    root.bind('<KeyPress-F3>', flashb3)
    c20.place(x=180,y=30,height=30,width=80)
    c9.config(bg='#6fedd0')
    def flashb4(event):
       c9.config(bg = 'green')
       root.after(175, lambda: c9.config(bg = '#6fedd0'))
       c9f()
    root.bind('<KeyPress-F4>', flashb4)
    c9.place(x=270,y=30,height=30,width=80)
    c11.config(bg='#6fedd0')
    def flashb5(event):
       c11.config(bg = 'green')
       root.after(175, lambda: c11.config(bg = '#6fedd0'))
       c11f()
    root.bind('<KeyPress-F5>', flashb5)
    c11.place(x=360,y=30,height=30,width=80)
    c13.config(bg='#6fedd0')
    def flashb6(event):
       c13.config(bg = 'green')
       root.after(175, lambda: c13.config(bg = '#6fedd0'))
       c13f()
    root.bind('<KeyPress-F6>', flashb6)
    c13.place(x=450,y=30,height=30,width=80)
    c27.config(bg='#6fedd0')
    def flashb7(event):
       c27.config(bg = 'green')
       root.after(175, lambda: c27.config(bg = '#6fedd0'))
       c27f()
    root.bind('<KeyPress-F7>', flashb7)
    c27.place(x=560,y=30,height=30,width=80)
    c40.config(bg='#6fedd0')
    def flashb8(event):
       c40.config(bg = 'green')
       root.after(175, lambda: c40.config(bg = '#6fedd0'))
       c40f()
    root.bind('<KeyPress-Q>', flashb8)
    c40.place(x=0,y=60,height=30,width=80)
    c54.config(bg='#6fedd0')
    def flashb9(event):
       c54.config(bg = 'green')
       root.after(175, lambda: c54.config(bg = '#6fedd0'))
       c54f()
    root.bind('<KeyPress-W>', flashb9)
    c54.place(x=90,y=60,height=30,width=80)
    c56.config(bg='#6fedd0')
    def flashb10(event):
       c56.config(bg = 'green')
       root.after(175, lambda: c56.config(bg = '#6fedd0'))
       c56f()
    root.bind('<KeyPress-E>', flashb10)
    c56.place(x=180,y=60,height=30,width=80)
    c45.config(bg='#6fedd0')
    def flashb11(event):
       c45.config(bg = 'green')
       root.after(175, lambda: c45.config(bg = '#6fedd0'))
       c45f()
    root.bind('<KeyPress-R>', flashb11)
    c45.place(x=270,y=60,height=30,width=80)
    c71.config(bg='#6fedd0')
    def flashb12(event):
       c71.config(bg = 'green')
       root.after(175, lambda: c71.config(bg = '#6fedd0'))
       c71f()
    root.bind('<KeyPress-T>', flashb12)
    c71.place(x=360,y=60,height=30,width=80)
    c49.config(bg='#6fedd0')
    def flashb13(event):
       c49.config(bg = 'green')
       root.after(175, lambda: c49.config(bg = '#6fedd0'))
       c49f()
    root.bind('<KeyPress-Y>', flashb13)
    c49.place(x=450,y=60,height=30,width=80)
    c75.config(bg='#6fedd0')
    def flashb14(event):
       c75.config(bg = 'green')
       root.after(175, lambda: c75.config(bg = '#6fedd0'))
       c75f()
    root.bind('<KeyPress-U>', flashb14)
    c75.place(x=560,y=60,height=30,width=80)
def showscale5():
    resetchords()
    resetpiano()
    global flag
    flag=5
    e_major_show()
    c5.config(bg='#e39ad8')
    def flashb1(event):
       c5.config(bg = 'green')
       root.after(175, lambda: c5.config(bg = '#e39ad8'))
       c5f()
    root.bind('<KeyPress-F1>', flashb1)
    c5.place(x=0,y=30,height=30,width=80)
    c19.config(bg='#e39ad8')
    def flashb2(event):
       c19.config(bg = 'green')
       root.after(175, lambda: c19.config(bg = '#e39ad8'))
       c19f()
    root.bind('<KeyPress-F2>', flashb2)
    c19.place(x=90,y=30,height=30,width=80)
    c21.config(bg='#e39ad8')
    def flashb3(event):
       c21.config(bg = 'green')
       root.after(175, lambda: c21.config(bg = '#e39ad8'))
       c21f()
    root.bind('<KeyPress-F3>', flashb3)
    c21.place(x=180,y=30,height=30,width=80)
    c10.config(bg='#e39ad8')
    def flashb4(event):
       c10.config(bg = 'green')
       root.after(175, lambda: c10.config(bg = '#e39ad8'))
       c10f()
    root.bind('<KeyPress-F4>', flashb4)
    c10.place(x=270,y=30,height=30,width=80)
    c12.config(bg='#e39ad8')
    def flashb5(event):
       c12.config(bg = 'green')
       root.after(175, lambda: c12.config(bg = '#e39ad8'))
       c12f()
    root.bind('<KeyPress-F5>', flashb5)
    c12.place(x=360,y=30,height=30,width=80)
    c14.config(bg='#e39ad8')
    def flashb6(event):
       c14.config(bg = 'green')
       root.after(175, lambda: c14.config(bg = '#e39ad8'))
       c14f()
    root.bind('<KeyPress-F6>', flashb6)
    c14.place(x=450,y=30,height=30,width=80)
    c28.config(bg='#e39ad8')
    def flashb7(event):
       c28.config(bg = 'green')
       root.after(175, lambda: c28.config(bg = '#e39ad8'))
       c28f()
    root.bind('<KeyPress-F7>', flashb7)
    c28.place(x=560,y=30,height=30,width=80)
    c41.config(bg='#e39ad8')
    def flashb8(event):
       c41.config(bg = 'green')
       root.after(175, lambda: c41.config(bg = '#e39ad8'))
       c41f()
    root.bind('<KeyPress-Q>', flashb8)
    c41.place(x=0,y=60,height=30,width=80)
    c55.config(bg='#e39ad8')
    def flashb9(event):
       c55.config(bg = 'green')
       root.after(175, lambda: c55.config(bg = '#e39ad8'))
       c55f()
    root.bind('<KeyPress-W>', flashb9)
    c55.place(x=90,y=60,height=30,width=80)
    c57.config(bg='#e39ad8')
    def flashb10(event):
       c57.config(bg = 'green')
       root.after(175, lambda: c57.config(bg = '#e39ad8'))
       c57f()
    root.bind('<KeyPress-E>', flashb10)
    c57.place(x=180,y=60,height=30,width=80)
    c46.config(bg='#e39ad8')
    def flashb11(event):
       c46.config(bg = 'green')
       root.after(175, lambda: c46.config(bg = '#e39ad8'))
       c46f()
    root.bind('<KeyPress-R>', flashb11)
    c46.place(x=270,y=60,height=30,width=80)
    c72.config(bg='#e39ad8')
    def flashb12(event):
       c72.config(bg = 'green')
       root.after(175, lambda: c72.config(bg = '#e39ad8'))
       c72f()
    root.bind('<KeyPress-T>', flashb12)
    c72.place(x=360,y=60,height=30,width=80)
    c50.config(bg='#e39ad8')
    def flashb13(event):
       c50.config(bg = 'green')
       root.after(175, lambda: c50.config(bg = '#e39ad8'))
       c50f()
    root.bind('<KeyPress-Y>', flashb13)
    c50.place(x=450,y=60,height=30,width=80)
    c76.config(bg='#e39ad8')
    def flashb14(event):
       c76.config(bg = 'green')
       root.after(175, lambda: c76.config(bg = '#e39ad8'))
       c76f()
    root.bind('<KeyPress-U>', flashb14)
    c76.place(x=560,y=60,height=30,width=80)
def showscale6():
    resetchords()
    resetpiano()
    global flag
    flag=6
    f_major_show()
    c6.config(bg='#ffc830')
    def flashb1(event):
       c6.config(bg = 'green')
       root.after(175, lambda: c6.config(bg = '#ffc830'))
       c6f()
    root.bind('<KeyPress-F1>', flashb1)
    c6.place(x=0,y=30,height=30,width=80)
    c20.config(bg='#ffc830')
    def flashb2(event):
       c20.config(bg = 'green')
       root.after(175, lambda: c20.config(bg = '#ffc830'))
       c20f()
    root.bind('<KeyPress-F2>', flashb2)
    c20.place(x=90,y=30,height=30,width=80)
    c22.config(bg='#ffc830')
    def flashb3(event):
       c22.config(bg = 'green')
       root.after(175, lambda: c22.config(bg = '#ffc830'))
       c22f()
    root.bind('<KeyPress-F3>', flashb3)
    c22.place(x=180,y=30,height=30,width=80)
    c11.config(bg='#ffc830')
    def flashb4(event):
       c11.config(bg = 'green')
       root.after(175, lambda: c11.config(bg = '#ffc830'))
       c11f()
    root.bind('<KeyPress-F4>', flashb4)
    c11.place(x=270,y=30,height=30,width=80)
    c1.config(bg='#ffc830')
    def flashb5(event):
       c1.config(bg = 'green')
       root.after(175, lambda: c1.config(bg = '#ffc830'))
       c1f()
    root.bind('<KeyPress-F5>', flashb5)
    c1.place(x=360,y=30,height=30,width=80)
    c15.config(bg='#ffc830')
    def flashb6(event):
       c15.config(bg = 'green')
       root.after(175, lambda: c15.config(bg = '#ffc830'))
       c15f()
    root.bind('<KeyPress-F6>', flashb6)
    c15.place(x=450,y=30,height=30,width=80)
    c29.config(bg='#ffc830')
    def flashb7(event):
       c29.config(bg = 'green')
       root.after(175, lambda: c29.config(bg = '#ffc830'))
       c29f()
    root.bind('<KeyPress-F7>', flashb7)
    c29.place(x=560,y=30,height=30,width=80)
    c42.config(bg='#ffc830')
    def flashb8(event):
       c42.config(bg = 'green')
       root.after(175, lambda: c42.config(bg = '#ffc830'))
       c42f()
    root.bind('<KeyPress-Q>', flashb8)
    c42.place(x=0,y=60,height=30,width=80)
    c56.config(bg='#ffc830')
    def flashb9(event):
       c56.config(bg = 'green')
       root.after(175, lambda: c56.config(bg = '#ffc830'))
       c56f()
    root.bind('<KeyPress-W>', flashb9)
    c56.place(x=90,y=60,height=30,width=80)
    c58.config(bg='#ffc830')
    def flashb10(event):
       c58.config(bg = 'green')
       root.after(175, lambda: c58.config(bg = '#ffc830'))
       c58f()
    root.bind('<KeyPress-E>', flashb10)
    c58.place(x=180,y=60,height=30,width=80)
    c47.config(bg='#ffc830')
    def flashb11(event):
       c47.config(bg = 'green')
       root.after(175, lambda: c47.config(bg = '#ffc830'))
       c47f()
    root.bind('<KeyPress-R>', flashb11)
    c47.place(x=270,y=60,height=30,width=80)
    c61.config(bg='#ffc830')
    def flashb12(event):
       c61.config(bg = 'green')
       root.after(175, lambda: c61.config(bg = '#ffc830'))
       c61f()
    root.bind('<KeyPress-T>', flashb12)
    c61.place(x=360,y=60,height=30,width=80)
    c51.config(bg='#ffc830')
    def flashb13(event):
       c51.config(bg = 'green')
       root.after(175, lambda: c51.config(bg = '#ffc830'))
       c51f()
    root.bind('<KeyPress-Y>', flashb13)
    c51.place(x=450,y=60,height=30,width=80)
    c77.config(bg='#ffc830')
    def flashb14(event):
       c77.config(bg = 'green')
       root.after(175, lambda: c77.config(bg = '#ffc830'))
       c77f()
    root.bind('<KeyPress-U>', flashb14)
    c77.place(x=560,y=60,height=30,width=80)
def showscale7():
    resetchords()
    resetpiano()
    global flag
    flag=7
    f_sharp_major_show()
    c7.config(bg='#f5f071')
    def flashb1(event):
       c7.config(bg = 'green')
       root.after(175, lambda: c7.config(bg = '#f5f071'))
       c7f()
    root.bind('<KeyPress-F1>', flashb1)
    c7.place(x=0,y=30,height=30,width=80)
    c21.config(bg='#f5f071')
    def flashb2(event):
       c21.config(bg = 'green')
       root.after(175, lambda: c21.config(bg = '#f5f071'))
       c21f()
    root.bind('<KeyPress-F2>', flashb2)
    c21.place(x=90,y=30,height=30,width=80)
    c23.config(bg='#f5f071')
    def flashb3(event):
       c23.config(bg = 'green')
       root.after(175, lambda: c23.config(bg = '#f5f071'))
       c23f()
    root.bind('<KeyPress-F3>', flashb3)
    c23.place(x=180,y=30,height=30,width=80)
    c12.config(bg='#f5f071')
    def flashb4(event):
       c12.config(bg = 'green')
       root.after(175, lambda: c12.config(bg = '#f5f071'))
       c12f()
    root.bind('<KeyPress-F4>', flashb4)
    c12.place(x=270,y=30,height=30,width=80)
    c2.config(bg='#f5f071')
    def flashb5(event):
       c2.config(bg = 'green')
       root.after(175, lambda: c2.config(bg = '#f5f071'))
       c2f()
    root.bind('<KeyPress-F5>', flashb5)
    c2.place(x=360,y=30,height=30,width=80)
    c16.config(bg='#f5f071')
    def flashb6(event):
       c16.config(bg = 'green')
       root.after(175, lambda: c16.config(bg = '#f5f071'))
       c16f()
    root.bind('<KeyPress-F6>', flashb6)
    c16.place(x=450,y=30,height=30,width=80)
    c30.config(bg='#f5f071')
    def flashb7(event):
       c30.config(bg = 'green')
       root.after(175, lambda: c30.config(bg = '#f5f071'))
       c30f()
    root.bind('<KeyPress-F7>', flashb7)
    c30.place(x=560,y=30,height=30,width=80)
    c43.config(bg='#f5f071')
    def flashb8(event):
       c43.config(bg = 'green')
       root.after(175, lambda: c43.config(bg = '#f5f071'))
       c43f()
    root.bind('<KeyPress-Q>', flashb8)
    c43.place(x=0,y=60,height=30,width=80)
    c57.config(bg='#f5f071')
    def flashb9(event):
       c57.config(bg = 'green')
       root.after(175, lambda: c57.config(bg = '#f5f071'))
       c57f()
    root.bind('<KeyPress-W>', flashb9)
    c57.place(x=90,y=60,height=30,width=80)
    c59.config(bg='#f5f071')
    def flashb10(event):
       c59.config(bg = 'green')
       root.after(175, lambda: c59.config(bg = '#f5f071'))
       c59f()
    root.bind('<KeyPress-E>', flashb10)
    c59.place(x=180,y=60,height=30,width=80)
    c48.config(bg='#f5f071')
    def flashb11(event):
       c48.config(bg = 'green')
       root.after(175, lambda: c48.config(bg = '#f5f071'))
       c48f()
    root.bind('<KeyPress-R>', flashb11)
    c48.place(x=270,y=60,height=30,width=80)
    c62.config(bg='#f5f071')
    def flashb12(event):
       c62.config(bg = 'green')
       root.after(175, lambda: c62.config(bg = '#f5f071'))
       c62f()
    root.bind('<KeyPress-T>', flashb12)
    c62.place(x=360,y=60,height=30,width=80)
    c52.config(bg='#f5f071')
    def flashb13(event):
       c52.config(bg = 'green')
       root.after(175, lambda: c52.config(bg = '#f5f071'))
       c52f()
    root.bind('<KeyPress-Y>', flashb13)
    c52.place(x=450,y=60,height=30,width=80)
    c78.config(bg='#f5f071')
    def flashb14(event):
       c78.config(bg = 'green')
       root.after(175, lambda: c78.config(bg = '#f5f071'))
       c78f()
    root.bind('<KeyPress-U>', flashb14)
    c78.place(x=560,y=60,height=30,width=80)
def showscale8():
    resetchords()
    resetpiano()
    global flag
    flag=8
    g_major_show()
    c8.config(bg='#a8edaf')
    def flashb1(event):
       c8.config(bg = 'green')
       root.after(175, lambda: c8.config(bg = '#a8edaf'))
       c8f()
    root.bind('<KeyPress-F1>', flashb1)
    c8.place(x=0,y=30,height=30,width=80)
    c22.config(bg='#a8edaf')
    def flashb2(event):
       c22.config(bg = 'green')
       root.after(175, lambda: c22.config(bg = '#a8edaf'))
       c22f()
    root.bind('<KeyPress-F2>', flashb2)
    c22.place(x=90,y=30,height=30,width=80)
    c24.config(bg='#a8edaf')
    def flashb3(event):
       c24.config(bg = 'green')
       root.after(175, lambda: c24.config(bg = '#a8edaf'))
       c24f()
    root.bind('<KeyPress-F3>', flashb3)
    c24.place(x=180,y=30,height=30,width=80)
    c1.config(bg='#a8edaf')
    def flashb4(event):
       c1.config(bg = 'green')
       root.after(175, lambda: c1.config(bg = '#a8edaf'))
       c1f()
    root.bind('<KeyPress-F4>', flashb4)
    c1.place(x=270,y=30,height=30,width=80)
    c3.config(bg='#a8edaf')
    def flashb5(event):
       c3.config(bg = 'green')
       root.after(175, lambda: c3.config(bg = '#a8edaf'))
       c3f()
    root.bind('<KeyPress-F5>', flashb5)
    c3.place(x=360,y=30,height=30,width=80)
    c17.config(bg='#a8edaf')
    def flashb6(event):
       c17.config(bg = 'green')
       root.after(175, lambda: c17.config(bg = '#a8edaf'))
       c17f()
    root.bind('<KeyPress-F6>', flashb6)
    c17.place(x=450,y=30,height=30,width=80)
    c31.config(bg='#a8edaf')
    def flashb7(event):
       c31.config(bg = 'green')
       root.after(175, lambda: c31.config(bg = '#a8edaf'))
       c31f()
    root.bind('<KeyPress-F7>', flashb7)
    c31.place(x=560,y=30,height=30,width=80)
    c44.config(bg='#a8edaf')
    def flashb8(event):
       c44.config(bg = 'green')
       root.after(175, lambda: c44.config(bg = '#a8edaf'))
       c44f()
    root.bind('<KeyPress-Q>', flashb8)
    c44.place(x=0,y=60,height=30,width=80)
    c58.config(bg='#a8edaf')
    def flashb9(event):
       c58.config(bg = 'green')
       root.after(175, lambda: c58.config(bg = '#a8edaf'))
       c58f()
    root.bind('<KeyPress-W>', flashb9)
    c58.place(x=90,y=60,height=30,width=80)
    c60.config(bg='#a8edaf')
    def flashb10(event):
       c60.config(bg = 'green')
       root.after(175, lambda: c60.config(bg = '#a8edaf'))
       c60f()
    root.bind('<KeyPress-E>', flashb10)
    c60.place(x=180,y=60,height=30,width=80)
    c37.config(bg='#a8edaf')
    def flashb11(event):
       c37.config(bg = 'green')
       root.after(175, lambda: c37.config(bg = '#a8edaf'))
       c37f()
    root.bind('<KeyPress-R>', flashb11)
    c37.place(x=270,y=60,height=30,width=80)
    c63.config(bg='#a8edaf')
    def flashb12(event):
       c63.config(bg = 'green')
       root.after(175, lambda: c63.config(bg = '#a8edaf'))
       c63f()
    root.bind('<KeyPress-T>', flashb12)
    c63.place(x=360,y=60,height=30,width=80)
    c53.config(bg='#a8edaf')
    def flashb13(event):
       c53.config(bg = 'green')
       root.after(175, lambda: c53.config(bg = '#a8edaf'))
       c53f()
    root.bind('<KeyPress-Y>', flashb13)
    c53.place(x=450,y=60,height=30,width=80)
    c79.config(bg='#a8edaf')
    def flashb14(event):
       c79.config(bg = 'green')
       root.after(175, lambda: c79.config(bg = '#a8edaf'))
       c79f()
    root.bind('<KeyPress-U>', flashb14)
    c79.place(x=560,y=60,height=30,width=80)
def showscale9():
    resetchords()
    resetpiano()
    global flag
    flag=9
    g_sharp_major_show()
    c9.config(bg='#90b5f0')
    def flashb1(event):
       c9.config(bg = 'green')
       root.after(175, lambda: c9.config(bg = '#90b5f0'))
       c9f()
    root.bind('<KeyPress-F1>', flashb1)
    c9.place(x=0,y=30,height=30,width=80)
    c23.config(bg='#90b5f0')
    def flashb2(event):
       c23.config(bg = 'green')
       root.after(175, lambda: c23.config(bg = '#90b5f0'))
       c23f()
    root.bind('<KeyPress-F2>', flashb2)
    c23.place(x=90,y=30,height=30,width=80)
    c13.config(bg='#90b5f0')
    def flashb3(event):
       c13.config(bg = 'green')
       root.after(175, lambda: c13.config(bg = '#90b5f0'))
       c13f()
    root.bind('<KeyPress-F3>', flashb3)
    c13.place(x=180,y=30,height=30,width=80)
    c2.config(bg='#90b5f0')
    def flashb4(event):
       c2.config(bg = 'green')
       root.after(175, lambda: c2.config(bg = '#90b5f0'))
       c2f()
    root.bind('<KeyPress-F4>', flashb4)
    c2.place(x=270,y=30,height=30,width=80)
    c4.config(bg='#90b5f0')
    def flashb5(event):
       c4.config(bg = 'green')
       root.after(175, lambda: c4.config(bg = '#90b5f0'))
       c4f()
    root.bind('<KeyPress-F5>', flashb5)
    c4.place(x=360,y=30,height=30,width=80)
    c18.config(bg='#90b5f0')
    def flashb6(event):
       c18.config(bg = 'green')
       root.after(175, lambda: c18.config(bg = '#90b5f0'))
       c18f()
    root.bind('<KeyPress-F6>', flashb6)
    c18.place(x=450,y=30,height=30,width=80)
    c32.config(bg='#90b5f0')
    def flashb7(event):
       c32.config(bg = 'green')
       root.after(175, lambda: c32.config(bg = '#90b5f0'))
       c32f()
    root.bind('<KeyPress-F7>', flashb7)
    c32.place(x=560,y=30,height=30,width=80)
    c45.config(bg='#90b5f0')
    def flashb8(event):
       c45.config(bg = 'green')
       root.after(175, lambda: c45.config(bg = '#90b5f0'))
       c45f()
    root.bind('<KeyPress-Q>', flashb8)
    c45.place(x=0,y=60,height=30,width=80)
    c59.config(bg='#90b5f0')
    def flashb9(event):
       c59.config(bg = 'green')
       root.after(175, lambda: c59.config(bg = '#90b5f0'))
       c59f()
    root.bind('<KeyPress-W>', flashb9)
    c59.place(x=90,y=60,height=30,width=80)
    c49.config(bg='#90b5f0')
    def flashb10(event):
       c49.config(bg = 'green')
       root.after(175, lambda: c49.config(bg = '#90b5f0'))
       c49f()
    root.bind('<KeyPress-E>', flashb10)
    c49.place(x=180,y=60,height=30,width=80)
    c38.config(bg='#90b5f0')
    def flashb11(event):
       c38.config(bg = 'green')
       root.after(175, lambda: c38.config(bg = '#90b5f0'))
       c38f()
    root.bind('<KeyPress-R>', flashb11)
    c38.place(x=270,y=60,height=30,width=80)
    c64.config(bg='#90b5f0')
    def flashb12(event):
       c64.config(bg = 'green')
       root.after(175, lambda: c64.config(bg = '#90b5f0'))
       c64f()
    root.bind('<KeyPress-T>', flashb12)
    c64.place(x=360,y=60,height=30,width=80)
    c54.config(bg='#90b5f0')
    def flashb13(event):
       c54.config(bg = 'green')
       root.after(175, lambda: c54.config(bg = '#90b5f0'))
       c54f()
    root.bind('<KeyPress-Y>', flashb13)
    c54.place(x=450,y=60,height=30,width=80)
    c80.config(bg='#90b5f0')
    def flashb14(event):
       c80.config(bg = 'green')
       root.after(175, lambda: c80.config(bg = '#90b5f0'))
       c80f()
    root.bind('<KeyPress-U>', flashb14)
    c80.place(x=560,y=60,height=30,width=80)
def showscale10():
    resetchords()
    resetpiano()
    global flag
    flag=10
    a_major_show()
    c10.config(bg='#e6d375')
    def flashb1(event):
       c10.config(bg = 'green')
       root.after(175, lambda: c10.config(bg = '#e6d375'))
       c10f()
    root.bind('<KeyPress-F1>', flashb1)
    c10.place(x=0,y=30,height=30,width=80)
    c24.config(bg='#e6d375')
    def flashb2(event):
       c24.config(bg = 'green')
       root.after(175, lambda: c24.config(bg = '#e6d375'))
       c24f()
    root.bind('<KeyPress-F2>', flashb2)
    c24.place(x=90,y=30,height=30,width=80)
    c14.config(bg='#e6d375')
    def flashb3(event):
       c14.config(bg = 'green')
       root.after(175, lambda: c14.config(bg = '#e6d375'))
       c14f()
    root.bind('<KeyPress-F3>', flashb3)
    c14.place(x=180,y=30,height=30,width=80)
    c3.config(bg='#e6d375')
    def flashb4(event):
       c3.config(bg = 'green')
       root.after(175, lambda: c3.config(bg = '#e6d375'))
       c3f()
    root.bind('<KeyPress-F4>', flashb4)
    c3.place(x=270,y=30,height=30,width=80)
    c5.config(bg='#e6d375')
    def flashb5(event):
       c5.config(bg = 'green')
       root.after(175, lambda: c5.config(bg = '#e6d375'))
       c5f()
    root.bind('<KeyPress-F5>', flashb5)
    c5.place(x=360,y=30,height=30,width=80)
    c19.config(bg='#e6d375')
    def flashb6(event):
       c19.config(bg = 'green')
       root.after(175, lambda: c19.config(bg = '#e6d375'))
       c19f()
    root.bind('<KeyPress-F6>', flashb6)
    c19.place(x=450,y=30,height=30,width=80)
    c33.config(bg='#e6d375')
    def flashb7(event):
       c33.config(bg = 'green')
       root.after(175, lambda: c33.config(bg = '#e6d375'))
       c33f()
    root.bind('<KeyPress-F7>', flashb7)
    c33.place(x=560,y=30,height=30,width=80)
    c46.config(bg='#e6d375')
    def flashb8(event):
       c46.config(bg = 'green')
       root.after(175, lambda: c46.config(bg = '#e6d375'))
       c46f()
    root.bind('<KeyPress-Q>', flashb8)
    c46.place(x=0,y=60,height=30,width=80)
    c60.config(bg='#e6d375')
    def flashb9(event):
       c60.config(bg = 'green')
       root.after(175, lambda: c60.config(bg = '#e6d375'))
       c60f()
    root.bind('<KeyPress-W>', flashb9)
    c60.place(x=90,y=60,height=30,width=80)
    c50.config(bg='#e6d375')
    def flashb10(event):
       c50.config(bg = 'green')
       root.after(175, lambda: c50.config(bg = '#e6d375'))
       c50f()
    root.bind('<KeyPress-E>', flashb10)
    c50.place(x=180,y=60,height=30,width=80)
    c39.config(bg='#e6d375')
    def flashb11(event):
       c39.config(bg = 'green')
       root.after(175, lambda: c39.config(bg = '#e6d375'))
       c39f()
    root.bind('<KeyPress-R>', flashb11)
    c39.place(x=270,y=60,height=30,width=80)
    c65.config(bg='#e6d375')
    def flashb12(event):
       c65.config(bg = 'green')
       root.after(175, lambda: c65.config(bg = '#e6d375'))
       c65f()
    root.bind('<KeyPress-T>', flashb12)
    c65.place(x=360,y=60,height=30,width=80)
    c55.config(bg='#e6d375')
    def flashb13(event):
       c55.config(bg = 'green')
       root.after(175, lambda: c55.config(bg = '#e6d375'))
       c55f()
    root.bind('<KeyPress-Y>', flashb13)
    c55.place(x=450,y=60,height=30,width=80)
    c81.config(bg='#e6d375')
    def flashb14(event):
       c81.config(bg = 'green')
       root.after(175, lambda: c81.config(bg = '#e6d375'))
       c81f()
    root.bind('<KeyPress-U>', flashb14)
    c81.place(x=560,y=60,height=30,width=80)
def showscale11():
    resetchords()
    resetpiano()
    global flag
    flag=11
    a_sharp_major_show()
    c11.config(bg='#a0eb38')
    def flashb1(event):
       c11.config(bg = 'green')
       root.after(175, lambda: c11.config(bg = '#a0eb38'))
       c11f()
    root.bind('<KeyPress-F1>', flashb1)
    c11.place(x=0,y=30,height=30,width=80)
    c13.config(bg='#a0eb38')
    def flashb2(event):
       c13.config(bg = 'green')
       root.after(175, lambda: c13.config(bg = '#a0eb38'))
       c13f()
    root.bind('<KeyPress-F2>', flashb2)
    c13.place(x=90,y=30,height=30,width=80)
    c15.config(bg='#a0eb38')
    def flashb3(event):
       c15.config(bg = 'green')
       root.after(175, lambda: c15.config(bg = '#a0eb38'))
       c15f()
    root.bind('<KeyPress-F3>', flashb3)
    c15.place(x=180,y=30,height=30,width=80)
    c4.config(bg='#a0eb38')
    def flashb4(event):
       c4.config(bg = 'green')
       root.after(175, lambda: c4.config(bg = '#a0eb38'))
       c4f()
    root.bind('<KeyPress-F4>', flashb4)
    c4.place(x=270,y=30,height=30,width=80)
    c6.config(bg='#a0eb38')
    def flashb5(event):
       c6.config(bg = 'green')
       root.after(175, lambda: c6.config(bg = '#a0eb38'))
       c6f()
    root.bind('<KeyPress-F5>', flashb5)
    c6.place(x=360,y=30,height=30,width=80)
    c20.config(bg='#a0eb38')
    def flashb6(event):
       c20.config(bg = 'green')
       root.after(175, lambda: c20.config(bg = '#a0eb38'))
       c20f()
    root.bind('<KeyPress-F6>', flashb6)
    c20.place(x=450,y=30,height=30,width=80)
    c34.config(bg='#a0eb38')
    def flashb7(event):
       c34.config(bg = 'green')
       root.after(175, lambda: c34.config(bg = '#a0eb38'))
       c34f()
    root.bind('<KeyPress-F7>', flashb7)
    c34.place(x=560,y=30,height=30,width=80)
    c47.config(bg='#a0eb38')
    def flashb8(event):
       c47.config(bg = 'green')
       root.after(175, lambda: c47.config(bg = '#a0eb38'))
       c47f()
    root.bind('<KeyPress-Q>', flashb8)
    c47.place(x=0,y=60,height=30,width=80)
    c49.config(bg='#a0eb38')
    def flashb9(event):
       c49.config(bg = 'green')
       root.after(175, lambda: c49.config(bg = '#a0eb38'))
       c49f()
    root.bind('<KeyPress-W>', flashb9)
    c49.place(x=90,y=60,height=30,width=80)
    c51.config(bg='#a0eb38')
    def flashb10(event):
       c51.config(bg = 'green')
       root.after(175, lambda: c51.config(bg = '#a0eb38'))
       c51f()
    root.bind('<KeyPress-E>', flashb10)
    c51.place(x=180,y=60,height=30,width=80)
    c40.config(bg='#a0eb38')
    def flashb11(event):
       c40.config(bg = 'green')
       root.after(175, lambda: c40.config(bg = '#a0eb38'))
       c40f()
    root.bind('<KeyPress-R>', flashb11)
    c40.place(x=270,y=60,height=30,width=80)
    c66.config(bg='#a0eb38')
    def flashb12(event):
       c66.config(bg = 'green')
       root.after(175, lambda: c66.config(bg = '#a0eb38'))
       c66f()
    root.bind('<KeyPress-T>', flashb12)
    c66.place(x=360,y=60,height=30,width=80)
    c56.config(bg='#a0eb38')
    def flashb13(event):
       c56.config(bg = 'green')
       root.after(175, lambda: c56.config(bg = '#a0eb38'))
       c56f()
    root.bind('<KeyPress-Y>', flashb13)
    c56.place(x=450,y=60,height=30,width=80)
    c82.config(bg='#a0eb38')
    def flashb14(event):
       c82.config(bg = 'green')
       root.after(175, lambda: c82.config(bg = '#a0eb38'))
       c82f()
    root.bind('<KeyPress-U>', flashb14)
    c82.place(x=560,y=60,height=30,width=80)
def showscale12():
    resetchords()
    resetpiano()
    global flag
    flag=12
    b_major_show()
    c12.config(bg='#60eb85')
    def flashb1(event):
       c12.config(bg = 'green')
       root.after(175, lambda: c12.config(bg = '#60eb85'))
       c12f()
    root.bind('<KeyPress-F1>', flashb1)
    c12.place(x=0,y=30,height=30,width=80)
    c14.config(bg='#60eb85')
    def flashb2(event):
       c14.config(bg = 'green')
       root.after(175, lambda: c14.config(bg = '#60eb85'))
       c14f()
    root.bind('<KeyPress-F2>', flashb2)
    c14.place(x=90,y=30,height=30,width=80)
    c16.config(bg='#60eb85')
    def flashb3(event):
       c16.config(bg = 'green')
       root.after(175, lambda: c16.config(bg = '#60eb85'))
       c16f()
    root.bind('<KeyPress-F3>', flashb3)
    c16.place(x=180,y=30,height=30,width=80)
    c5.config(bg='#60eb85')
    def flashb4(event):
       c5.config(bg = 'green')
       root.after(175, lambda: c5.config(bg = '#60eb85'))
       c5f()
    root.bind('<KeyPress-F4>', flashb4)
    c5.place(x=270,y=30,height=30,width=80)
    c7.config(bg='#60eb85')
    def flashb5(event):
       c7.config(bg = 'green')
       root.after(175, lambda: c7.config(bg = '#60eb85'))
       c7f()
    root.bind('<KeyPress-F5>', flashb5)
    c7.place(x=360,y=30,height=30,width=80)
    c21.config(bg='#60eb85')
    def flashb6(event):
       c21.config(bg = 'green')
       root.after(175, lambda: c21.config(bg = '#60eb85'))
       c21f()
    root.bind('<KeyPress-F6>', flashb6)
    c21.place(x=450,y=30,height=30,width=80)
    c35.config(bg='#60eb85')
    def flashb7(event):
       c35.config(bg = 'green')
       root.after(175, lambda: c35.config(bg = '#60eb85'))
       c35f()
    root.bind('<KeyPress-F7>', flashb7)
    c35.place(x=560,y=30,height=30,width=80)
    c48.config(bg='#60eb85')
    def flashb8(event):
       c48.config(bg = 'green')
       root.after(175, lambda: c48.config(bg = '#60eb85'))
       c48f()
    root.bind('<KeyPress-Q>', flashb8)
    c48.place(x=0,y=60,height=30,width=80)
    c50.config(bg='#60eb85')
    def flashb9(event):
       c50.config(bg = 'green')
       root.after(175, lambda: c50.config(bg = '#60eb85'))
       c50f()
    root.bind('<KeyPress-W>', flashb9)
    c50.place(x=90,y=60,height=30,width=80)
    c52.config(bg='#60eb85')
    def flashb10(event):
       c52.config(bg = 'green')
       root.after(175, lambda: c52.config(bg = '#60eb85'))
       c52f()
    root.bind('<KeyPress-E>', flashb10)
    c52.place(x=180,y=60,height=30,width=80)
    c41.config(bg='#60eb85')
    def flashb11(event):
       c41.config(bg = 'green')
       root.after(175, lambda: c41.config(bg = '#60eb85'))
       c41f()
    root.bind('<KeyPress-R>', flashb11)
    c41.place(x=270,y=60,height=30,width=80)
    c67.config(bg='#60eb85')
    def flashb12(event):
       c67.config(bg = 'green')
       root.after(175, lambda: c67.config(bg = '#60eb85'))
       c67f()
    root.bind('<KeyPress-T>', flashb12)
    c67.place(x=360,y=60,height=30,width=80)
    c57.config(bg='#60eb85')
    def flashb13(event):
       c57.config(bg = 'green')
       root.after(175, lambda: c57.config(bg = '#60eb85'))
       c57f()
    root.bind('<KeyPress-Y>', flashb13)
    c57.place(x=450,y=60,height=30,width=80)
    c83.config(bg='#60eb85')
    def flashb14(event):
       c83.config(bg = 'green')
       root.after(175, lambda: c83.config(bg = '#60eb85'))
       c83f()
    root.bind('<KeyPress-U>', flashb14)
    c83.place(x=560,y=60,height=30,width=80)
##############main chord radio button bunction to chane guitar note color#######################
############################Radio Button for chords###############################################################
scale1show=Button(frame_chord,text='C',command=showscale1)
scale1show.place(x=60,y=0,width=80,height=25)

scale2show=Button(frame_chord,text='C#/Db',command=showscale2)
scale2show.place(x=145,y=0,width=80,height=25)

scale3show=Button(frame_chord,text='D',command=showscale3)
scale3show.place(x=230,y=0,width=80,height=25)

scale4show=Button(frame_chord,text='D#/Eb',command=showscale4)    
scale4show.place(x=315,y=0,width=80,height=25)

scale5show=Button(frame_chord,text='E',command=showscale5)    
scale5show.place(x=400,y=0,width=80,height=25)

scale6show=Button(frame_chord,text='F',command=showscale6)    
scale6show.place(x=485,y=0,width=80,height=25)

scale7show=Button(frame_chord,text='F#/Gb',command=showscale7)    
scale7show.place(x=570,y=0,width=80,height=25)

scale8show=Button(frame_chord,text='G',command=showscale8)    
scale8show.place(x=655,y=0,width=80,height=25)

scale9show=Button(frame_chord,text='G#/Ab',command=showscale9)    
scale9show.place(x=740,y=0,width=80,height=25)

scale10show=Button(frame_chord,text='A',command=showscale10)    
scale10show.place(x=825,y=0,width=80,height=25)

scale11show=Button(frame_chord,text='A#/Bb',command=showscale11)    
scale11show.place(x=910,y=0,width=80,height=25)

scale12show=Button(frame_chord,text='B',command=showscale12)    
scale12show.place(x=995,y=0,width=80,height=25)
################################################
def c_major_show():
    b_c.place_forget()
    b_c_h.place(x=0,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = 'yellow'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = 'yellow'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = 'yellow'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = 'yellow'))
    root.bind('<KeyPress-4>', flashb6)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = 'yellow'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = 'yellow'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = 'yellow'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = 'yellow'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = 'yellow'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = 'yellow'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = 'yellow'))
    root.bind('<KeyPress-q>', flashb18)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = 'yellow'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = 'yellow'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = 'yellow'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = 'yellow'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = 'yellow'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = 'yellow'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = 'yellow'))
    root.bind('<KeyPress-i>', flashb30)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = 'yellow'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = 'yellow'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = 'yellow'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = 'yellow'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = 'yellow'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = 'yellow'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = 'yellow'))
    root.bind('<KeyPress-g>', flashb42)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = 'yellow'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = 'yellow'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = 'yellow'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = 'yellow'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = 'yellow'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = 'yellow'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = 'yellow'))
    root.bind('<KeyPress-c>', flashb54)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = 'yellow'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = 'yellow'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = 'yellow'))
    root.bind('<KeyPress-n>', flashb60)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = 'yellow'))
    root.bind('<KeyPress-m>', flashb61) 
    b1.configure(background='yellow')
    b3.configure(background='yellow')
    b5.configure(background='yellow')
    b6.configure(background='yellow')
    b8.configure(background='yellow')
    b10.configure(background='yellow')
    b12.configure(background='yellow')
    b13.configure(background='yellow')
    b15.configure(background='yellow')
    b17.configure(background='yellow')
    b18.configure(background='yellow')
    b20.configure(background='yellow')
    b22.configure(background='yellow')
    b24.configure(background='yellow')
    b25.configure(background='yellow')
    b27.configure(background='yellow')
    b29.configure(background='yellow')
    b30.configure(background='yellow')
    b32.configure(background='yellow')
    b34.configure(background='yellow')
    b36.configure(background='yellow')
    b37.configure(background='yellow')
    b39.configure(background='yellow')
    b41.configure(background='yellow')
    b42.configure(background='yellow')
    b44.configure(background='yellow')
    b46.configure(background='yellow')
    b48.configure(background='yellow')
    b49.configure(background='yellow')
    b51.configure(background='yellow')
    b53.configure(background='yellow')
    b54.configure(background='yellow')
    b56.configure(background='yellow')
    b58.configure(background='yellow')
    b60.configure(background='yellow')
    b61.configure(background='yellow')
def c_major_yellow():
    b_c_h.place_forget()
    b_c.place(x=0,y=50,width=80)
    b1.configure(background=orig_color)
    b3.configure(background=orig_color)
    b5.configure(background=orig_color)
    b6.configure(background=orig_color)
    b8.configure(background=orig_color)
    b10.configure(background=orig_color)
    b12.configure(background=orig_color)
    b13.configure(background=orig_color)
    b15.configure(background=orig_color)
    b17.configure(background=orig_color)
    b18.configure(background=orig_color)
    b20.configure(background=orig_color)
    b22.configure(background=orig_color)
    b24.configure(background=orig_color)
    b25.configure(background=orig_color)
    b27.configure(background=orig_color)
    b29.configure(background=orig_color)
    b30.configure(background=orig_color)
    b32.configure(background=orig_color)
    b34.configure(background=orig_color)
    b36.configure(background=orig_color)
    b37.configure(background=orig_color)
    b39.configure(background=orig_color)
    b41.configure(background=orig_color)
    b42.configure(background=orig_color)
    b44.configure(background=orig_color)
    b46.configure(background=orig_color)
    b48.configure(background=orig_color)
    b49.configure(background=orig_color)
    b51.configure(background=orig_color)
    b53.configure(background=orig_color)
    b54.configure(background=orig_color)
    b56.configure(background=orig_color)
    b58.configure(background=orig_color)
    b60.configure(background=orig_color)
    b61.configure(background=orig_color)
def c_sharp_major_show():
    b_c_sharp.place_forget()
    b_c_sharp_h.place(x=100,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = 'orange'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = 'orange'))
    root.bind('<KeyPress-2>', flashb2)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = 'orange'))
    root.bind('<KeyPress-3>', flashb4)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = 'orange'))
    root.bind('<KeyPress-4>', flashb6)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = 'orange'))
    root.bind('<KeyPress-5>', flashb7)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = 'orange'))
    root.bind('<KeyPress-6>', flashb9)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = 'orange'))
    root.bind('<KeyPress-7>', flashb11)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = 'orange'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = 'orange'))
    root.bind('<KeyPress-9>', flashb14)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = 'orange'))
    root.bind('<KeyPress-0>', flashb16)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = 'orange'))
    root.bind('<KeyPress-q>', flashb18)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = 'orange'))
    root.bind('<KeyPress-w>', flashb19)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = 'orange'))
    root.bind('<KeyPress-e>', flashb21)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = 'orange'))
    root.bind('<KeyPress-r>', flashb23)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = 'orange'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = 'orange'))
    root.bind('<KeyPress-y>', flashb26)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = 'orange'))
    root.bind('<KeyPress-u>', flashb28)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = 'orange'))
    root.bind('<KeyPress-i>', flashb30)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = 'orange'))
    root.bind('<KeyPress-o>', flashb31)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = 'orange'))
    root.bind('<KeyPress-p>', flashb33)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = 'orange'))
    root.bind('<KeyPress-a>', flashb35)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = 'orange'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = 'orange'))
    root.bind('<KeyPress-d>', flashb38)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = 'orange'))
    root.bind('<KeyPress-f>', flashb40)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = 'orange'))
    root.bind('<KeyPress-g>', flashb42)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = 'orange'))
    root.bind('<KeyPress-h>', flashb43)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = 'orange'))
    root.bind('<KeyPress-j>', flashb45)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = 'orange'))
    root.bind('<KeyPress-k>', flashb47)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = 'orange'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = 'orange'))
    root.bind('<KeyPress-z>', flashb50)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = 'orange'))
    root.bind('<KeyPress-x>', flashb52)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = 'orange'))
    root.bind('<KeyPress-c>', flashb54)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = 'orange'))
    root.bind('<KeyPress-v>', flashb55)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = 'orange'))
    root.bind('<KeyPress-b>', flashb57)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = 'orange'))
    root.bind('<KeyPress-n>', flashb59)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = 'orange'))
    root.bind('<KeyPress-m>', flashb61)
    b1.configure(background='orange',foreground='black')
    b2.configure(background='orange',foreground='black')
    b4.configure(background='orange',foreground='black')
    b6.configure(background='orange',foreground='black')
    b7.configure(background='orange',foreground='black')
    b9.configure(background='orange',foreground='black')
    b11.configure(background='orange',foreground='black')
    b13.configure(background='orange',foreground='black')
    b14.configure(background='orange',foreground='black')
    b16.configure(background='orange',foreground='black')
    b18.configure(background='orange',foreground='black')
    b19.configure(background='orange',foreground='black')
    b21.configure(background='orange',foreground='black')
    b23.configure(background='orange',foreground='black')
    b25.configure(background='orange',foreground='black')
    b26.configure(background='orange',foreground='black')
    b28.configure(background='orange',foreground='black')
    b30.configure(background='orange',foreground='black')
    b31.configure(background='orange',foreground='black')
    b33.configure(background='orange',foreground='black')
    b35.configure(background='orange',foreground='black')
    b37.configure(background='orange',foreground='black')
    b38.configure(background='orange',foreground='black')
    b40.configure(background='orange',foreground='black')
    b42.configure(background='orange',foreground='black')
    b43.configure(background='orange',foreground='black')
    b45.configure(background='orange',foreground='black')
    b47.configure(background='orange',foreground='black')
    b49.configure(background='orange',foreground='black')
    b50.configure(background='orange',foreground='black')
    b52.configure(background='orange',foreground='black')
    b54.configure(background='orange',foreground='black')
    b55.configure(background='orange',foreground='black')
    b57.configure(background='orange',foreground='black')
    b59.configure(background='orange',foreground='black')
    b61.configure(background='orange',foreground='black')
def c_sharp_major_orange():
    b_c_sharp_h.place_forget()
    b_c_sharp.place(x=100,y=50,width=80)
    b1.configure(background=orig_color)    
    b2.configure(background='black',foreground='white')
    b3.configure(background=orig_color)
    b4.configure(background='black',foreground='white')
    b5.configure(background=orig_color)
    b6.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b8.configure(background=orig_color)
    b9.configure(background='black',foreground='white')
    b10.configure(background=orig_color)
    b11.configure(background='black',foreground='white')
    b12.configure(background=orig_color)
    b13.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b15.configure(background=orig_color)
    b16.configure(background='black',foreground='white')
    b17.configure(background=orig_color)
    b18.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b20.configure(background=orig_color)
    b21.configure(background='black',foreground='white')
    b22.configure(background=orig_color)
    b23.configure(background='black',foreground='white')
    b24.configure(background=orig_color)
    b25.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b27.configure(background=orig_color)
    b28.configure(background='black',foreground='white')
    b29.configure(background=orig_color)
    b30.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b32.configure(background=orig_color)
    b33.configure(background='black',foreground='white')
    b34.configure(background=orig_color)
    b35.configure(background='black',foreground='white')
    b36.configure(background=orig_color)
    b37.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b39.configure(background=orig_color)
    b40.configure(background='black',foreground='white')
    b41.configure(background=orig_color)
    b42.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b44.configure(background=orig_color)
    b45.configure(background='black',foreground='white')
    b46.configure(background=orig_color)
    b47.configure(background='black',foreground='white')
    b48.configure(background=orig_color)
    b49.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b51.configure(background=orig_color)
    b52.configure(background='black',foreground='white')
    b53.configure(background=orig_color)
    b54.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b56.configure(background=orig_color)
    b57.configure(background='black',foreground='white')
    b58.configure(background=orig_color)
    b59.configure(background='black',foreground='white')
    b60.configure(background=orig_color)
    b61.configure(background=orig_color)
def d_major_show():
    b_d.place_forget()
    b_d_h.place(x=200,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = '#41d95f'))
    root.bind('<KeyPress-1>', flashb2)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = '#41d95f'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = '#41d95f'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = '#41d95f'))
    root.bind('<KeyPress-4>', flashb7)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = '#41d95f'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = '#41d95f'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = '#41d95f'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = '#41d95f'))
    root.bind('<KeyPress-8>', flashb14)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = '#41d95f'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = '#41d95f'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = '#41d95f'))
    root.bind('<KeyPress-q>', flashb19)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = '#41d95f'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = '#41d95f'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = '#41d95f'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = '#41d95f'))
    root.bind('<KeyPress-t>', flashb26)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = '#41d95f'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = '#41d95f'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = '#41d95f'))
    root.bind('<KeyPress-i>', flashb31)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = '#41d95f'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = '#41d95f'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = '#41d95f'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = '#41d95f'))
    root.bind('<KeyPress-s>', flashb38)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = '#41d95f'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = '#41d95f'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = '#41d95f'))
    root.bind('<KeyPress-g>', flashb43)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = '#41d95f'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = '#41d95f'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = '#41d95f'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = '#41d95f'))
    root.bind('<KeyPress-l>', flashb50)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = '#41d95f'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = '#41d95f'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = '#41d95f'))
    root.bind('<KeyPress-c>', flashb55)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = '#41d95f'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = '#41d95f'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = '#41d95f'))
    root.bind('<KeyPress-n>', flashb60)
    b2.configure(background='#41d95f',foreground='black')
    b3.configure(background='#41d95f')
    b5.configure(background='#41d95f')
    b7.configure(background='#41d95f',foreground='black')
    b8.configure(background='#41d95f')
    b10.configure(background='#41d95f')
    b12.configure(background='#41d95f')
    b14.configure(background='#41d95f',foreground='black')
    b15.configure(background='#41d95f')
    b17.configure(background='#41d95f')
    b19.configure(background='#41d95f',foreground='black')
    b20.configure(background='#41d95f')
    b22.configure(background='#41d95f')
    b24.configure(background='#41d95f')
    b26.configure(background='#41d95f',foreground='black')
    b27.configure(background='#41d95f')
    b29.configure(background='#41d95f')
    b31.configure(background='#41d95f',foreground='black')
    b32.configure(background='#41d95f')
    b34.configure(background='#41d95f')
    b36.configure(background='#41d95f')
    b38.configure(background='#41d95f',foreground='black')
    b39.configure(background='#41d95f')
    b41.configure(background='#41d95f')
    b43.configure(background='#41d95f',foreground='black')
    b44.configure(background='#41d95f')
    b46.configure(background='#41d95f')
    b48.configure(background='#41d95f')
    b50.configure(background='#41d95f',foreground='black')
    b51.configure(background='#41d95f')
    b53.configure(background='#41d95f')
    b55.configure(background='#41d95f',foreground='black')
    b56.configure(background='#41d95f')
    b58.configure(background='#41d95f')
    b60.configure(background='#41d95f')

def d_major_e64040():
    b_d_h.place_forget()
    b_d.place(x=200,y=50,width=80)
    b2.configure(background='black',foreground='white')
    b3.configure(background=orig_color)
    b5.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b8.configure(background=orig_color)
    b10.configure(background=orig_color)
    b12.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b15.configure(background=orig_color)
    b17.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b20.configure(background=orig_color)
    b22.configure(background=orig_color)
    b24.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b27.configure(background=orig_color)
    b29.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b32.configure(background=orig_color)
    b34.configure(background=orig_color)
    b36.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b39.configure(background=orig_color)
    b41.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b44.configure(background=orig_color)
    b46.configure(background=orig_color)
    b48.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b51.configure(background=orig_color)
    b53.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b56.configure(background=orig_color)
    b58.configure(background=orig_color)
    b60.configure(background=orig_color)
def d_sharp_major_show():
    b_d_sharp.place_forget()
    b_d_sharp_h.place(x=300,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = '#6fedd0'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = '#6fedd0'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = '#6fedd0'))
    root.bind('<KeyPress-3>', flashb4)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = '#6fedd0'))
    root.bind('<KeyPress-4>', flashb6)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = '#6fedd0'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = '#6fedd0'))
    root.bind('<KeyPress-6>', flashb9)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = '#6fedd0'))
    root.bind('<KeyPress-7>', flashb11)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = '#6fedd0'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = '#6fedd0'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = '#6fedd0'))
    root.bind('<KeyPress-0>', flashb16)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = '#6fedd0'))
    root.bind('<KeyPress-q>', flashb18)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = '#6fedd0'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = '#6fedd0'))
    root.bind('<KeyPress-e>', flashb21)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = '#6fedd0'))
    root.bind('<KeyPress-r>', flashb23)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = '#6fedd0'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = '#6fedd0'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = '#6fedd0'))
    root.bind('<KeyPress-u>', flashb28)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = '#6fedd0'))
    root.bind('<KeyPress-i>', flashb30)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = '#6fedd0'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = '#6fedd0'))
    root.bind('<KeyPress-p>', flashb33)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = '#6fedd0'))
    root.bind('<KeyPress-a>', flashb35)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = '#6fedd0'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = '#6fedd0'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = '#6fedd0'))
    root.bind('<KeyPress-f>', flashb40)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = '#6fedd0'))
    root.bind('<KeyPress-g>', flashb42)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = '#6fedd0'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = '#6fedd0'))
    root.bind('<KeyPress-j>', flashb45)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = '#6fedd0'))
    root.bind('<KeyPress-k>', flashb47)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = '#6fedd0'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = '#6fedd0'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = '#6fedd0'))
    root.bind('<KeyPress-x>', flashb52)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = '#6fedd0'))
    root.bind('<KeyPress-c>', flashb54)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = '#6fedd0'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = '#6fedd0'))
    root.bind('<KeyPress-b>', flashb57)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = '#6fedd0'))
    root.bind('<KeyPress-n>', flashb59)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = '#6fedd0'))
    root.bind('<KeyPress-m>', flashb61)
    b1.configure(background='#6fedd0')    
    b3.configure(background='#6fedd0')
    b4.configure(background='#6fedd0',foreground='black')
    b6.configure(background='#6fedd0')
    b8.configure(background='#6fedd0')
    b9.configure(background='#6fedd0',foreground='black')
    b11.configure(background='#6fedd0',foreground='black')
    b13.configure(background='#6fedd0')
    b15.configure(background='#6fedd0')
    b16.configure(background='#6fedd0',foreground='black')
    b18.configure(background='#6fedd0')
    b20.configure(background='#6fedd0')
    b21.configure(background='#6fedd0',foreground='black')
    b23.configure(background='#6fedd0',foreground='black')
    b25.configure(background='#6fedd0')
    b27.configure(background='#6fedd0')
    b28.configure(background='#6fedd0',foreground='black')
    b30.configure(background='#6fedd0')
    b32.configure(background='#6fedd0')
    b33.configure(background='#6fedd0',foreground='black')
    b35.configure(background='#6fedd0',foreground='black')
    b37.configure(background='#6fedd0')
    b39.configure(background='#6fedd0')
    b40.configure(background='#6fedd0',foreground='black')
    b42.configure(background='#6fedd0')
    b44.configure(background='#6fedd0')
    b45.configure(background='#6fedd0',foreground='black')
    b47.configure(background='#6fedd0',foreground='black')
    b49.configure(background='#6fedd0')
    b51.configure(background='#6fedd0')
    b52.configure(background='#6fedd0',foreground='black')
    b54.configure(background='#6fedd0')
    b56.configure(background='#6fedd0')
    b57.configure(background='#6fedd0',foreground='black')
    b59.configure(background='#6fedd0',foreground='black')
    b61.configure(background='#6fedd0')
def d_sharp_major_6fedd0():
    b_d_sharp_h.place_forget()
    b_d_sharp.place(x=300,y=50,width=80)
    b1.configure(background=orig_color)
    b3.configure(background=orig_color)
    b4.configure(background='black',foreground='white')
    b6.configure(background=orig_color)
    b8.configure(background=orig_color)
    b9.configure(background='black',foreground='white')
    b11.configure(background='black',foreground='white')
    b13.configure(background=orig_color)
    b15.configure(background=orig_color)
    b16.configure(background='black',foreground='white')
    b18.configure(background=orig_color)
    b20.configure(background=orig_color)
    b21.configure(background='black',foreground='white')
    b23.configure(background='black',foreground='white')
    b25.configure(background=orig_color)
    b27.configure(background=orig_color)
    b28.configure(background='black',foreground='white')
    b30.configure(background=orig_color)
    b32.configure(background=orig_color)
    b33.configure(background='black',foreground='white')
    b35.configure(background='black',foreground='white')
    b37.configure(background=orig_color)
    b39.configure(background=orig_color)
    b40.configure(background='black',foreground='white')
    b42.configure(background=orig_color)
    b44.configure(background=orig_color)
    b45.configure(background='black',foreground='white')
    b47.configure(background='black',foreground='white')
    b49.configure(background=orig_color)
    b51.configure(background=orig_color)
    b52.configure(background='black',foreground='white')
    b54.configure(background=orig_color)
    b56.configure(background=orig_color)
    b57.configure(background='black',foreground='white')
    b59.configure(background='black',foreground='white')
    b61.configure(background=orig_color)
def e_major_show():
    b_e.place_forget()
    b_e_h.place(x=400,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = '#e39ad8'))
    root.bind('<KeyPress-1>', flashb2)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = '#e39ad8'))
    root.bind('<KeyPress-2>', flashb4)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = '#e39ad8'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = '#e39ad8'))
    root.bind('<KeyPress-4>', flashb7)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = '#e39ad8'))
    root.bind('<KeyPress-5>', flashb9)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = '#e39ad8'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = '#e39ad8'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = '#e39ad8'))
    root.bind('<KeyPress-8>', flashb14)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = '#e39ad8'))
    root.bind('<KeyPress-9>', flashb16)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = '#e39ad8'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = '#e39ad8'))
    root.bind('<KeyPress-q>', flashb19)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = '#e39ad8'))
    root.bind('<KeyPress-w>', flashb21)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = '#e39ad8'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = '#e39ad8'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = '#e39ad8'))
    root.bind('<KeyPress-t>', flashb26)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = '#e39ad8'))
    root.bind('<KeyPress-y>', flashb28)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = '#e39ad8'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = '#e39ad8'))
    root.bind('<KeyPress-i>', flashb31)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = '#e39ad8'))
    root.bind('<KeyPress-o>', flashb33)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = '#e39ad8'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = '#e39ad8'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = '#e39ad8'))
    root.bind('<KeyPress-s>', flashb38)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = '#e39ad8'))
    root.bind('<KeyPress-d>', flashb40)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = '#e39ad8'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = '#e39ad8'))
    root.bind('<KeyPress-g>', flashb43)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = '#e39ad8'))
    root.bind('<KeyPress-h>', flashb45)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = '#e39ad8'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = '#e39ad8'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = '#e39ad8'))
    root.bind('<KeyPress-l>', flashb50)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = '#e39ad8'))
    root.bind('<KeyPress-z>', flashb52)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = '#e39ad8'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = '#e39ad8'))
    root.bind('<KeyPress-c>', flashb55)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = '#e39ad8'))
    root.bind('<KeyPress-v>', flashb57)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = '#e39ad8'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = '#e39ad8'))
    root.bind('<KeyPress-n>', flashb60)
    b2.configure(background='#e39ad8',foreground='black')
    b4.configure(background='#e39ad8',foreground='black')
    b5.configure(background='#e39ad8')
    b7.configure(background='#e39ad8',foreground='black')
    b9.configure(background='#e39ad8',foreground='black')
    b10.configure(background='#e39ad8')
    b12.configure(background='#e39ad8')
    b14.configure(background='#e39ad8',foreground='black')
    b16.configure(background='#e39ad8',foreground='black')
    b17.configure(background='#e39ad8')
    b19.configure(background='#e39ad8',foreground='black')
    b21.configure(background='#e39ad8',foreground='black')
    b22.configure(background='#e39ad8')
    b24.configure(background='#e39ad8')
    b26.configure(background='#e39ad8',foreground='black')
    b28.configure(background='#e39ad8',foreground='black')
    b29.configure(background='#e39ad8')
    b31.configure(background='#e39ad8',foreground='black')
    b33.configure(background='#e39ad8',foreground='black')
    b34.configure(background='#e39ad8')
    b36.configure(background='#e39ad8')
    b38.configure(background='#e39ad8',foreground='black')
    b40.configure(background='#e39ad8',foreground='black')
    b41.configure(background='#e39ad8')
    b43.configure(background='#e39ad8',foreground='black')
    b45.configure(background='#e39ad8',foreground='black')
    b46.configure(background='#e39ad8')
    b48.configure(background='#e39ad8')
    b50.configure(background='#e39ad8',foreground='black')
    b52.configure(background='#e39ad8',foreground='black')
    b53.configure(background='#e39ad8')
    b55.configure(background='#e39ad8',foreground='black')
    b57.configure(background='#e39ad8',foreground='black')
    b58.configure(background='#e39ad8')
    b60.configure(background='#e39ad8')
def e_major_e39ad8():
    b_e_h.place_forget()
    b_e.place(x=400,y=50,width=80)
    b2.configure(background='black',foreground='white')
    b4.configure(background='black',foreground='white')
    b5.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b9.configure(background='black',foreground='white')
    b10.configure(background=orig_color)
    b12.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b16.configure(background='black',foreground='white')
    b17.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b21.configure(background='black',foreground='white')
    b22.configure(background=orig_color)
    b24.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b28.configure(background='black',foreground='white')
    b29.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b33.configure(background='black',foreground='white')
    b34.configure(background=orig_color)
    b36.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b40.configure(background='black',foreground='white')
    b41.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b45.configure(background='black',foreground='white')
    b46.configure(background=orig_color)
    b48.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b52.configure(background='black',foreground='white')
    b53.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b57.configure(background='black',foreground='white')
    b58.configure(background=orig_color)
    b60.configure(background=orig_color)
def f_major_show():
    b_f.place_forget()
    b_f_h.place(x=500,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = '#ffc830'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = '#ffc830'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = '#ffc830'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = '#ffc830'))
    root.bind('<KeyPress-4>', flashb6)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = '#ffc830'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = '#ffc830'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = '#ffc830'))
    root.bind('<KeyPress-7>', flashb11)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = '#ffc830'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = '#ffc830'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = '#ffc830'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = '#ffc830'))
    root.bind('<KeyPress-q>', flashb18)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = '#ffc830'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = '#ffc830'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = '#ffc830'))
    root.bind('<KeyPress-r>', flashb23)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = '#ffc830'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = '#ffc830'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = '#ffc830'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = '#ffc830'))
    root.bind('<KeyPress-i>', flashb30)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = '#ffc830'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = '#ffc830'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = '#ffc830'))
    root.bind('<KeyPress-a>', flashb35)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = '#ffc830'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = '#ffc830'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = '#ffc830'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = '#ffc830'))
    root.bind('<KeyPress-g>', flashb42)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = '#ffc830'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = '#ffc830'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = '#ffc830'))
    root.bind('<KeyPress-k>', flashb47)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = '#ffc830'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = '#ffc830'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = '#ffc830'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = '#ffc830'))
    root.bind('<KeyPress-c>', flashb54)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = '#ffc830'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = '#ffc830'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = '#ffc830'))
    root.bind('<KeyPress-n>', flashb59)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = '#ffc830'))
    root.bind('<KeyPress-m>', flashb61)
    b1.configure(background='#ffc830')
    b3.configure(background='#ffc830')
    b5.configure(background='#ffc830')
    b6.configure(background='#ffc830')
    b8.configure(background='#ffc830')
    b10.configure(background='#ffc830')
    b11.configure(background='#ffc830',foreground='black')
    b13.configure(background='#ffc830')
    b15.configure(background='#ffc830')
    b17.configure(background='#ffc830')
    b18.configure(background='#ffc830')
    b20.configure(background='#ffc830')
    b22.configure(background='#ffc830')
    b23.configure(background='#ffc830',foreground='black')
    b25.configure(background='#ffc830')
    b27.configure(background='#ffc830')
    b29.configure(background='#ffc830')
    b30.configure(background='#ffc830')
    b32.configure(background='#ffc830')
    b34.configure(background='#ffc830')
    b35.configure(background='#ffc830',foreground='black')
    b37.configure(background='#ffc830')
    b39.configure(background='#ffc830')
    b41.configure(background='#ffc830')
    b42.configure(background='#ffc830')
    b44.configure(background='#ffc830')
    b46.configure(background='#ffc830')
    b47.configure(background='#ffc830',foreground='black')
    b49.configure(background='#ffc830')
    b51.configure(background='#ffc830')
    b53.configure(background='#ffc830')
    b54.configure(background='#ffc830')
    b56.configure(background='#ffc830')
    b58.configure(background='#ffc830')
    b59.configure(background='#ffc830',foreground='black')
    b61.configure(background='#ffc830')
def f_major_ffc830():
    b_f_h.place_forget()
    b_f.place(x=500,y=50,width=80)
    b1.configure(background=orig_color)
    b3.configure(background=orig_color)
    b5.configure(background=orig_color)
    b6.configure(background=orig_color)
    b8.configure(background=orig_color)
    b10.configure(background=orig_color)
    b11.configure(background='black',foreground='white')
    b13.configure(background=orig_color)
    b15.configure(background=orig_color)
    b17.configure(background=orig_color)
    b18.configure(background=orig_color)
    b20.configure(background=orig_color)
    b22.configure(background=orig_color)
    b23.configure(background='black',foreground='white')
    b25.configure(background=orig_color)
    b27.configure(background=orig_color)
    b29.configure(background=orig_color)
    b30.configure(background=orig_color)
    b32.configure(background=orig_color)
    b34.configure(background=orig_color)
    b35.configure(background='black',foreground='white')
    b37.configure(background=orig_color)
    b39.configure(background=orig_color)
    b41.configure(background=orig_color)
    b42.configure(background=orig_color)
    b44.configure(background=orig_color)
    b46.configure(background=orig_color)
    b47.configure(background='black',foreground='white')
    b49.configure(background=orig_color)
    b51.configure(background=orig_color)
    b53.configure(background=orig_color)
    b54.configure(background=orig_color)
    b56.configure(background=orig_color)
    b58.configure(background=orig_color)
    b59.configure(background='black',foreground='white')
    b61.configure(background=orig_color)
def f_sharp_major_show():
    b_f_sharp.place_forget()
    b_f_sharp_h.place(x=600,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = '#f5f071'))
    root.bind('<KeyPress-1>', flashb2)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = '#f5f071'))
    root.bind('<KeyPress-2>', flashb4)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = '#f5f071'))
    root.bind('<KeyPress-3>', flashb6)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = '#f5f071'))
    root.bind('<KeyPress-4>', flashb7)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = '#f5f071'))
    root.bind('<KeyPress-5>', flashb9)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = '#f5f071'))
    root.bind('<KeyPress-6>', flashb11)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = '#f5f071'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = '#f5f071'))
    root.bind('<KeyPress-8>', flashb14)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = '#f5f071'))
    root.bind('<KeyPress-9>', flashb16)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = '#f5f071'))
    root.bind('<KeyPress-0>', flashb18)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = '#f5f071'))
    root.bind('<KeyPress-q>', flashb19)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = '#f5f071'))
    root.bind('<KeyPress-w>', flashb21)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = '#f5f071'))
    root.bind('<KeyPress-e>', flashb23)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = '#f5f071'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = '#f5f071'))
    root.bind('<KeyPress-t>', flashb26)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = '#f5f071'))
    root.bind('<KeyPress-y>', flashb28)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = '#f5f071'))
    root.bind('<KeyPress-u>', flashb30)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = '#f5f071'))
    root.bind('<KeyPress-i>', flashb31)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = '#f5f071'))
    root.bind('<KeyPress-o>', flashb33)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = '#f5f071'))
    root.bind('<KeyPress-p>', flashb35)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = '#f5f071'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = '#f5f071'))
    root.bind('<KeyPress-s>', flashb38)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = '#f5f071'))
    root.bind('<KeyPress-d>', flashb40)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = '#f5f071'))
    root.bind('<KeyPress-f>', flashb42)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = '#f5f071'))
    root.bind('<KeyPress-g>', flashb43)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = '#f5f071'))
    root.bind('<KeyPress-h>', flashb45)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = '#f5f071'))
    root.bind('<KeyPress-j>', flashb47)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = '#f5f071'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = '#f5f071'))
    root.bind('<KeyPress-l>', flashb50)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = '#f5f071'))
    root.bind('<KeyPress-z>', flashb52)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = '#f5f071'))
    root.bind('<KeyPress-x>', flashb54)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = '#f5f071'))
    root.bind('<KeyPress-c>', flashb55)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = '#f5f071'))
    root.bind('<KeyPress-v>', flashb57)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = '#f5f071'))
    root.bind('<KeyPress-b>', flashb59)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = '#f5f071'))
    root.bind('<KeyPress-n>', flashb60)
    b2.configure(background='#f5f071',foreground='black')
    b4.configure(background='#f5f071',foreground='black')
    b6.configure(background='#f5f071')
    b7.configure(background='#f5f071',foreground='black')
    b9.configure(background='#f5f071',foreground='black')
    b11.configure(background='#f5f071',foreground='black')
    b12.configure(background='#f5f071')
    b14.configure(background='#f5f071',foreground='black')
    b16.configure(background='#f5f071',foreground='black')
    b18.configure(background='#f5f071')
    b19.configure(background='#f5f071',foreground='black')
    b21.configure(background='#f5f071',foreground='black')
    b23.configure(background='#f5f071',foreground='black')
    b24.configure(background='#f5f071')
    b26.configure(background='#f5f071',foreground='black')
    b28.configure(background='#f5f071',foreground='black')
    b30.configure(background='#f5f071')
    b31.configure(background='#f5f071',foreground='black')
    b33.configure(background='#f5f071',foreground='black')
    b35.configure(background='#f5f071',foreground='black')
    b36.configure(background='#f5f071')
    b38.configure(background='#f5f071',foreground='black')
    b40.configure(background='#f5f071',foreground='black')
    b42.configure(background='#f5f071')
    b43.configure(background='#f5f071',foreground='black')
    b45.configure(background='#f5f071',foreground='black')
    b47.configure(background='#f5f071',foreground='black')
    b48.configure(background='#f5f071')
    b50.configure(background='#f5f071',foreground='black')
    b52.configure(background='#f5f071',foreground='black')
    b54.configure(background='#f5f071')
    b55.configure(background='#f5f071',foreground='black')
    b57.configure(background='#f5f071',foreground='black')
    b59.configure(background='#f5f071',foreground='black')
    b60.configure(background='#f5f071')
def f_sharp_major_f7929a():
    b_f_sharp_h.place_forget()
    b_f_sharp.place(x=600,y=50,width=80)
    b2.configure(background='black',foreground='white')
    b4.configure(background='black',foreground='white')
    b6.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b9.configure(background='black',foreground='white')
    b11.configure(background='black',foreground='white')
    b12.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b16.configure(background='black',foreground='white')
    b18.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b21.configure(background='black',foreground='white')
    b23.configure(background='black',foreground='white')
    b24.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b28.configure(background='black',foreground='white')
    b30.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b33.configure(background='black',foreground='white')
    b35.configure(background='black',foreground='white')
    b36.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b40.configure(background='black',foreground='white')
    b42.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b45.configure(background='black',foreground='white')
    b47.configure(background='black',foreground='white')
    b48.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b52.configure(background='black',foreground='white')
    b54.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b57.configure(background='black',foreground='white')
    b59.configure(background='black',foreground='white')
    b60.configure(background=orig_color)
def g_major_show():
    b_g.place_forget()
    b_g_h.place(x=700,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = '#a8edaf'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = '#a8edaf'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = '#a8edaf'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = '#a8edaf'))
    root.bind('<KeyPress-4>', flashb7)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = '#a8edaf'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = '#a8edaf'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = '#a8edaf'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = '#a8edaf'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = '#a8edaf'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = '#a8edaf'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = '#a8edaf'))
    root.bind('<KeyPress-q>', flashb19)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = '#a8edaf'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = '#a8edaf'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = '#a8edaf'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = '#a8edaf'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = '#a8edaf'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = '#a8edaf'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = '#a8edaf'))
    root.bind('<KeyPress-i>', flashb31)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = '#a8edaf'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = '#a8edaf'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = '#a8edaf'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = '#a8edaf'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = '#a8edaf'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = '#a8edaf'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = '#a8edaf'))
    root.bind('<KeyPress-g>', flashb43)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = '#a8edaf'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = '#a8edaf'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = '#a8edaf'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = '#a8edaf'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = '#a8edaf'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = '#a8edaf'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = '#a8edaf'))
    root.bind('<KeyPress-c>', flashb55)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = '#a8edaf'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = '#a8edaf'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = '#a8edaf'))
    root.bind('<KeyPress-n>', flashb60)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = '#a8edaf'))
    root.bind('<KeyPress-m>', flashb61)
    b1.configure(background='#a8edaf')
    b3.configure(background='#a8edaf')
    b5.configure(background='#a8edaf')
    b7.configure(background='#a8edaf',foreground='black')
    b8.configure(background='#a8edaf')
    b10.configure(background='#a8edaf')
    b12.configure(background='#a8edaf')
    b13.configure(background='#a8edaf')
    b15.configure(background='#a8edaf')
    b17.configure(background='#a8edaf')
    b19.configure(background='#a8edaf',foreground='black')
    b20.configure(background='#a8edaf')
    b22.configure(background='#a8edaf')
    b24.configure(background='#a8edaf')
    b25.configure(background='#a8edaf')
    b27.configure(background='#a8edaf')
    b29.configure(background='#a8edaf')
    b31.configure(background='#a8edaf',foreground='black')
    b32.configure(background='#a8edaf')
    b34.configure(background='#a8edaf')
    b36.configure(background='#a8edaf')
    b37.configure(background='#a8edaf')
    b39.configure(background='#a8edaf')
    b41.configure(background='#a8edaf')
    b43.configure(background='#a8edaf',foreground='black')
    b44.configure(background='#a8edaf')
    b46.configure(background='#a8edaf')
    b48.configure(background='#a8edaf')
    b49.configure(background='#a8edaf')
    b51.configure(background='#a8edaf')
    b53.configure(background='#a8edaf')
    b55.configure(background='#a8edaf',foreground='black')
    b56.configure(background='#a8edaf')
    b58.configure(background='#a8edaf')
    b60.configure(background='#a8edaf')
    b61.configure(background='#a8edaf')
def g_major_a8edaf():
    b_g_h.place_forget()
    b_g.place(x=700,y=50,width=80)
    b1.configure(background=orig_color)    
    b3.configure(background=orig_color)
    b5.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b8.configure(background=orig_color)
    b10.configure(background=orig_color)
    b12.configure(background=orig_color)
    b13.configure(background=orig_color)
    b15.configure(background=orig_color)
    b17.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b20.configure(background=orig_color)
    b22.configure(background=orig_color)
    b24.configure(background=orig_color)
    b25.configure(background=orig_color)
    b27.configure(background=orig_color)
    b29.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b32.configure(background=orig_color)
    b34.configure(background=orig_color)
    b36.configure(background=orig_color)
    b37.configure(background=orig_color)
    b39.configure(background=orig_color)
    b41.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b44.configure(background=orig_color)
    b46.configure(background=orig_color)
    b48.configure(background=orig_color)
    b49.configure(background=orig_color)
    b51.configure(background=orig_color)
    b53.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b56.configure(background=orig_color)
    b58.configure(background=orig_color)
    b60.configure(background=orig_color)
    b61.configure(background=orig_color)
def g_sharp_major_show():
    b_g_sharp.place_forget()
    b_g_sharp_h.place(x=800,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = '#90b5f0'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = '#90b5f0'))
    root.bind('<KeyPress-2>', flashb2)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = '#90b5f0'))
    root.bind('<KeyPress-3>', flashb4)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = '#90b5f0'))
    root.bind('<KeyPress-4>', flashb6)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = '#90b5f0'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = '#90b5f0'))
    root.bind('<KeyPress-6>', flashb9)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = '#90b5f0'))
    root.bind('<KeyPress-7>', flashb11)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = '#90b5f0'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = '#90b5f0'))
    root.bind('<KeyPress-9>', flashb14)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = '#90b5f0'))
    root.bind('<KeyPress-0>', flashb16)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = '#90b5f0'))
    root.bind('<KeyPress-q>', flashb18)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = '#90b5f0'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = '#90b5f0'))
    root.bind('<KeyPress-e>', flashb21)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = '#90b5f0'))
    root.bind('<KeyPress-r>', flashb23)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = '#90b5f0'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = '#90b5f0'))
    root.bind('<KeyPress-y>', flashb26)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = '#90b5f0'))
    root.bind('<KeyPress-u>', flashb28)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = '#90b5f0'))
    root.bind('<KeyPress-i>', flashb30)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = '#90b5f0'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = '#90b5f0'))
    root.bind('<KeyPress-p>', flashb33)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = '#90b5f0'))
    root.bind('<KeyPress-a>', flashb35)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = '#90b5f0'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = '#90b5f0'))
    root.bind('<KeyPress-d>', flashb38)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = '#90b5f0'))
    root.bind('<KeyPress-f>', flashb40)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = '#90b5f0'))
    root.bind('<KeyPress-g>', flashb42)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = '#90b5f0'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = '#90b5f0'))
    root.bind('<KeyPress-j>', flashb45)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = '#90b5f0'))
    root.bind('<KeyPress-k>', flashb47)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = '#90b5f0'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = '#90b5f0'))
    root.bind('<KeyPress-z>', flashb50)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = '#90b5f0'))
    root.bind('<KeyPress-x>', flashb52)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = '#90b5f0'))
    root.bind('<KeyPress-c>', flashb54)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = '#90b5f0'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = '#90b5f0'))
    root.bind('<KeyPress-b>', flashb57)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = '#90b5f0'))
    root.bind('<KeyPress-n>', flashb59)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = '#90b5f0'))
    root.bind('<KeyPress-m>', flashb61)
    b1.configure(background='#90b5f0',foreground='black')
    b2.configure(background='#90b5f0',foreground='black')
    b4.configure(background='#90b5f0',foreground='black')
    b6.configure(background='#90b5f0')
    b8.configure(background='#90b5f0')
    b9.configure(background='#90b5f0',foreground='black')
    b11.configure(background='#90b5f0',foreground='black')
    b13.configure(background='#90b5f0')
    b14.configure(background='#90b5f0',foreground='black')
    b16.configure(background='#90b5f0',foreground='black')
    b18.configure(background='#90b5f0')
    b20.configure(background='#90b5f0')
    b21.configure(background='#90b5f0',foreground='black')
    b23.configure(background='#90b5f0',foreground='black')
    b25.configure(background='#90b5f0')
    b26.configure(background='#90b5f0',foreground='black')
    b28.configure(background='#90b5f0',foreground='black')
    b30.configure(background='#90b5f0')
    b32.configure(background='#90b5f0')
    b33.configure(background='#90b5f0',foreground='black')
    b35.configure(background='#90b5f0',foreground='black')
    b37.configure(background='#90b5f0')
    b38.configure(background='#90b5f0',foreground='black')
    b40.configure(background='#90b5f0',foreground='black')
    b42.configure(background='#90b5f0')
    b44.configure(background='#90b5f0')
    b45.configure(background='#90b5f0',foreground='black')
    b47.configure(background='#90b5f0',foreground='black')
    b49.configure(background='#90b5f0')
    b50.configure(background='#90b5f0',foreground='black')
    b52.configure(background='#90b5f0',foreground='black')
    b54.configure(background='#90b5f0')
    b56.configure(background='#90b5f0')
    b57.configure(background='#90b5f0',foreground='black')
    b59.configure(background='#90b5f0',foreground='black')
    b61.configure(background='#90b5f0')
def g_sharp_major_d9a49a():
    b_g_sharp_h.place_forget()
    b_g_sharp.place(x=800,y=50,width=80)
    b1.configure(background=orig_color)
    b2.configure(background='black',foreground='white')
    b4.configure(background='black',foreground='white')
    b6.configure(background=orig_color)
    b8.configure(background=orig_color)
    b9.configure(background='black',foreground='white')
    b11.configure(background='black',foreground='white')
    b13.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b16.configure(background='black',foreground='white')
    b18.configure(background=orig_color)
    b20.configure(background=orig_color)
    b21.configure(background='black',foreground='white')
    b23.configure(background='black',foreground='white')
    b25.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b28.configure(background='black',foreground='white')
    b30.configure(background=orig_color)
    b32.configure(background=orig_color)
    b33.configure(background='black',foreground='white')
    b35.configure(background='black',foreground='white')
    b37.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b40.configure(background='black',foreground='white')
    b42.configure(background=orig_color)
    b44.configure(background=orig_color)
    b45.configure(background='black',foreground='white')
    b47.configure(background='black',foreground='white')
    b49.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b52.configure(background='black',foreground='white')
    b54.configure(background=orig_color)
    b56.configure(background=orig_color)
    b57.configure(background='black',foreground='white')
    b59.configure(background='black',foreground='white')
    b61.configure(background=orig_color)
def a_major_show():
    b_a.place_forget()
    b_a_h.place(x=900,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = '#e6d375'))
    root.bind('<KeyPress-1>', flashb2)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = '#e6d375'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = '#e6d375'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = '#e6d375'))
    root.bind('<KeyPress-4>', flashb7)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = '#e6d375'))
    root.bind('<KeyPress-5>', flashb9)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = '#e6d375'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = '#e6d375'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = '#e6d375'))
    root.bind('<KeyPress-8>', flashb14)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = '#e6d375'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = '#e6d375'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = '#e6d375'))
    root.bind('<KeyPress-q>', flashb19)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = '#e6d375'))
    root.bind('<KeyPress-w>', flashb21)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = '#e6d375'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = '#e6d375'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = '#e6d375'))
    root.bind('<KeyPress-t>', flashb26)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = '#e6d375'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = '#e6d375'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = '#e6d375'))
    root.bind('<KeyPress-i>', flashb31)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = '#e6d375'))
    root.bind('<KeyPress-o>', flashb33)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = '#e6d375'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = '#e6d375'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = '#e6d375'))
    root.bind('<KeyPress-s>', flashb38)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = '#e6d375'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = '#e6d375'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = '#e6d375'))
    root.bind('<KeyPress-g>', flashb43)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = '#e6d375'))
    root.bind('<KeyPress-h>', flashb45)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = '#e6d375'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = '#e6d375'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = '#e6d375'))
    root.bind('<KeyPress-l>', flashb50)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = '#e6d375'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = '#e6d375'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = '#e6d375'))
    root.bind('<KeyPress-c>', flashb55)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = '#e6d375'))
    root.bind('<KeyPress-v>', flashb57)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = '#e6d375'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = '#e6d375'))
    root.bind('<KeyPress-n>', flashb60)
    b2.configure(background='#e6d375',foreground='black')
    b3.configure(background='#e6d375')
    b5.configure(background='#e6d375')
    b7.configure(background='#e6d375',foreground='black')
    b9.configure(background='#e6d375',foreground='black')
    b10.configure(background='#e6d375')
    b12.configure(background='#e6d375')
    b14.configure(background='#e6d375',foreground='black')
    b15.configure(background='#e6d375')
    b17.configure(background='#e6d375')
    b19.configure(background='#e6d375',foreground='black')
    b21.configure(background='#e6d375',foreground='black')
    b22.configure(background='#e6d375')
    b24.configure(background='#e6d375')
    b26.configure(background='#e6d375',foreground='black')
    b27.configure(background='#e6d375')
    b29.configure(background='#e6d375')
    b31.configure(background='#e6d375',foreground='black')
    b33.configure(background='#e6d375',foreground='black')
    b34.configure(background='#e6d375')
    b36.configure(background='#e6d375')
    b38.configure(background='#e6d375',foreground='black')
    b39.configure(background='#e6d375')
    b41.configure(background='#e6d375')
    b43.configure(background='#e6d375',foreground='black')
    b45.configure(background='#e6d375',foreground='black')
    b46.configure(background='#e6d375')
    b48.configure(background='#e6d375')
    b50.configure(background='#e6d375',foreground='black')
    b51.configure(background='#e6d375')
    b53.configure(background='#e6d375')
    b55.configure(background='#e6d375',foreground='black')
    b57.configure(background='#e6d375',foreground='black')
    b58.configure(background='#e6d375')
    b60.configure(background='#e6d375')
def a_major_e6d375():
    b_a_h.place_forget()
    b_a.place(x=900,y=50,width=80)

    resetpiano()
    resetflash()
    b2.configure(background='black',foreground='white')
    b3.configure(background=orig_color)
    b5.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b9.configure(background='black',foreground='white')
    b10.configure(background=orig_color)
    b12.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b15.configure(background=orig_color)
    b17.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b21.configure(background='black',foreground='white')
    b22.configure(background=orig_color)
    b24.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b27.configure(background=orig_color)
    b29.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b33.configure(background='black',foreground='white')
    b34.configure(background=orig_color)
    b36.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b39.configure(background=orig_color)
    b41.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b45.configure(background='black',foreground='white')
    b46.configure(background=orig_color)
    b48.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b51.configure(background=orig_color)
    b53.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b57.configure(background='black',foreground='white')
    b58.configure(background=orig_color)
    b60.configure(background=orig_color)
def a_sharp_major_show():
    b_a_sharp.place_forget()
    b_a_sharp_h.place(x=1000,y=50,width=80)

    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb1(event):
       g1()
       b1.config(bg = 'green')
       root.after(175, lambda: b1.config(bg = '#a0eb38'))
    root.bind('<KeyPress-1>', flashb1)
    def flashb3(event):
       g3()
       b3.config(bg = 'green')
       root.after(175, lambda: b3.config(bg = '#a0eb38'))
    root.bind('<KeyPress-2>', flashb3)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = '#a0eb38'))
    root.bind('<KeyPress-3>', flashb4)
    def flashb6(event):
       g6()
       b6.config(bg = 'green')
       root.after(175, lambda: b6.config(bg = '#a0eb38'))
    root.bind('<KeyPress-4>', flashb6)
    def flashb8(event):
       g8()
       b8.config(bg = 'green')
       root.after(175, lambda: b8.config(bg = '#a0eb38'))
    root.bind('<KeyPress-5>', flashb8)
    def flashb10(event):
       g10()
       b10.config(bg = 'green')
       root.after(175, lambda: b10.config(bg = '#a0eb38'))
    root.bind('<KeyPress-6>', flashb10)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = '#a0eb38'))
    root.bind('<KeyPress-7>', flashb11)
    def flashb13(event):
       g13()
       b13.config(bg = 'green')
       root.after(175, lambda: b13.config(bg = '#a0eb38'))
    root.bind('<KeyPress-8>', flashb13)
    def flashb15(event):
       g15()
       b15.config(bg = 'green')
       root.after(175, lambda: b15.config(bg = '#a0eb38'))
    root.bind('<KeyPress-9>', flashb15)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = '#a0eb38'))
    root.bind('<KeyPress-0>', flashb16)
    def flashb18(event):
       g18()
       b18.config(bg = 'green')
       root.after(175, lambda: b18.config(bg = '#a0eb38'))
    root.bind('<KeyPress-q>', flashb18)
    def flashb20(event):
       g20()
       b20.config(bg = 'green')
       root.after(175, lambda: b20.config(bg = '#a0eb38'))
    root.bind('<KeyPress-w>', flashb20)
    def flashb22(event):
       g22()
       b22.config(bg = 'green')
       root.after(175, lambda: b22.config(bg = '#a0eb38'))
    root.bind('<KeyPress-e>', flashb22)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = '#a0eb38'))
    root.bind('<KeyPress-r>', flashb23)
    def flashb25(event):
       g25()
       b25.config(bg = 'green')
       root.after(175, lambda: b25.config(bg = '#a0eb38'))
    root.bind('<KeyPress-t>', flashb25)
    def flashb27(event):
       g27()
       b27.config(bg = 'green')
       root.after(175, lambda: b27.config(bg = '#a0eb38'))
    root.bind('<KeyPress-y>', flashb27)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = '#a0eb38'))
    root.bind('<KeyPress-u>', flashb28)
    def flashb30(event):
       g30()
       b30.config(bg = 'green')
       root.after(175, lambda: b30.config(bg = '#a0eb38'))
    root.bind('<KeyPress-i>', flashb30)
    def flashb32(event):
       g32()
       b32.config(bg = 'green')
       root.after(175, lambda: b32.config(bg = '#a0eb38'))
    root.bind('<KeyPress-o>', flashb32)
    def flashb34(event):
       g34()
       b34.config(bg = 'green')
       root.after(175, lambda: b34.config(bg = '#a0eb38'))
    root.bind('<KeyPress-p>', flashb34)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = '#a0eb38'))
    root.bind('<KeyPress-a>', flashb35)
    def flashb37(event):
       g37()
       b37.config(bg = 'green')
       root.after(175, lambda: b37.config(bg = '#a0eb38'))
    root.bind('<KeyPress-s>', flashb37)
    def flashb39(event):
       g39()
       b39.config(bg = 'green')
       root.after(175, lambda: b39.config(bg = '#a0eb38'))
    root.bind('<KeyPress-d>', flashb39)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = '#a0eb38'))
    root.bind('<KeyPress-f>', flashb40)
    def flashb42(event):
       g42()
       b42.config(bg = 'green')
       root.after(175, lambda: b42.config(bg = '#a0eb38'))
    root.bind('<KeyPress-g>', flashb42)
    def flashb44(event):
       g44()
       b44.config(bg = 'green')
       root.after(175, lambda: b44.config(bg = '#a0eb38'))
    root.bind('<KeyPress-h>', flashb44)
    def flashb46(event):
       g46()
       b46.config(bg = 'green')
       root.after(175, lambda: b46.config(bg = '#a0eb38'))
    root.bind('<KeyPress-j>', flashb46)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = '#a0eb38'))
    root.bind('<KeyPress-k>', flashb47)
    def flashb49(event):
       g49()
       b49.config(bg = 'green')
       root.after(175, lambda: b49.config(bg = '#a0eb38'))
    root.bind('<KeyPress-l>', flashb49)
    def flashb51(event):
       g51()
       b51.config(bg = 'green')
       root.after(175, lambda: b51.config(bg = '#a0eb38'))
    root.bind('<KeyPress-z>', flashb51)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = '#a0eb38'))
    root.bind('<KeyPress-x>', flashb52)
    def flashb54(event):
       g54()
       b54.config(bg = 'green')
       root.after(175, lambda: b54.config(bg = '#a0eb38'))
    root.bind('<KeyPress-c>', flashb54)
    def flashb56(event):
       g56()
       b56.config(bg = 'green')
       root.after(175, lambda: b56.config(bg = '#a0eb38'))
    root.bind('<KeyPress-v>', flashb56)
    def flashb58(event):
       g58()
       b58.config(bg = 'green')
       root.after(175, lambda: b58.config(bg = '#a0eb38'))
    root.bind('<KeyPress-b>', flashb58)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = '#a0eb38'))
    root.bind('<KeyPress-n>', flashb59)
    def flashb61(event):
       g61()
       b61.config(bg = 'green')
       root.after(175, lambda: b61.config(bg = '#a0eb38'))
    root.bind('<KeyPress-m>', flashb61)
    b1.configure(background='#a0eb38')
    b3.configure(background='#a0eb38')
    b4.configure(background='#a0eb38',foreground='black')
    b6.configure(background='#a0eb38')
    b8.configure(background='#a0eb38')
    b10.configure(background='#a0eb38')
    b11.configure(background='#a0eb38',foreground='black')
    b13.configure(background='#a0eb38')
    b15.configure(background='#a0eb38')
    b16.configure(background='#a0eb38',foreground='black')
    b18.configure(background='#a0eb38')
    b20.configure(background='#a0eb38')
    b22.configure(background='#a0eb38')
    b23.configure(background='#a0eb38',foreground='black')
    b25.configure(background='#a0eb38')
    b27.configure(background='#a0eb38')
    b28.configure(background='#a0eb38',foreground='black')
    b30.configure(background='#a0eb38')
    b32.configure(background='#a0eb38')
    b34.configure(background='#a0eb38')
    b35.configure(background='#a0eb38',foreground='black')
    b37.configure(background='#a0eb38')
    b39.configure(background='#a0eb38')
    b40.configure(background='#a0eb38',foreground='black')
    b42.configure(background='#a0eb38')
    b44.configure(background='#a0eb38')
    b46.configure(background='#a0eb38')
    b47.configure(background='#a0eb38',foreground='black')
    b49.configure(background='#a0eb38')
    b51.configure(background='#a0eb38')
    b52.configure(background='#a0eb38',foreground='black')
    b54.configure(background='#a0eb38')
    b56.configure(background='#a0eb38')
    b58.configure(background='#a0eb38')
    b59.configure(background='#a0eb38',foreground='black')
    b61.configure(background='#a0eb38')
def a_sharp_major_a0eb38():
    b_a_sharp_h.place_forget()
    b_a_sharp.place(x=1000,y=50,width=80)
    b1.configure(background=orig_color)    
    b3.configure(background=orig_color)
    b4.configure(background='black',foreground='white')
    b6.configure(background=orig_color)
    b8.configure(background=orig_color)
    b10.configure(background=orig_color)
    b11.configure(background='black',foreground='white')
    b13.configure(background=orig_color)
    b15.configure(background=orig_color)
    b16.configure(background='black',foreground='white')
    b18.configure(background=orig_color)
    b20.configure(background=orig_color)
    b22.configure(background=orig_color)
    b23.configure(background='black',foreground='white')
    b25.configure(background=orig_color)
    b27.configure(background=orig_color)
    b28.configure(background='black',foreground='white')
    b30.configure(background=orig_color)
    b32.configure(background=orig_color)
    b34.configure(background=orig_color)
    b35.configure(background='black',foreground='white')
    b37.configure(background=orig_color)
    b39.configure(background=orig_color)
    b40.configure(background='black',foreground='white')
    b42.configure(background=orig_color)
    b44.configure(background=orig_color)
    b46.configure(background=orig_color)
    b47.configure(background='black',foreground='white')
    b49.configure(background=orig_color)
    b51.configure(background=orig_color)
    b52.configure(background='black',foreground='white')
    b54.configure(background=orig_color)
    b56.configure(background=orig_color)
    b58.configure(background=orig_color)
    b59.configure(background='black',foreground='white')
    b61.configure(background=orig_color)
def b_major_show():
    b_b.place_forget()
    b_b_h.place(x=1100,y=50,width=80)
    resetpiano()
    resetflash()
    def flashb0(event):
       chordmute()
       stopchannels()
    root.bind('<KeyPress-space>', flashb0)
    def flashb2(event):
       g2()
       b2.config(bg = 'green')
       root.after(175, lambda: b2.config(bg = '#60eb85'))
    root.bind('<KeyPress-1>', flashb2)
    def flashb4(event):
       g4()
       b4.config(bg = 'green')
       root.after(175, lambda: b4.config(bg = '#60eb85'))
    root.bind('<KeyPress-2>', flashb4)
    def flashb5(event):
       g5()
       b5.config(bg = 'green')
       root.after(175, lambda: b5.config(bg = '#60eb85'))
    root.bind('<KeyPress-3>', flashb5)
    def flashb7(event):
       g7()
       b7.config(bg = 'green')
       root.after(175, lambda: b7.config(bg = '#60eb85'))
    root.bind('<KeyPress-4>', flashb7)
    def flashb9(event):
       g9()
       b9.config(bg = 'green')
       root.after(175, lambda: b9.config(bg = '#60eb85'))
    root.bind('<KeyPress-5>', flashb9)
    def flashb11(event):
       g11()
       b11.config(bg = 'green')
       root.after(175, lambda: b11.config(bg = '#60eb85'))
    root.bind('<KeyPress-6>', flashb11)
    def flashb12(event):
       g12()
       b12.config(bg = 'green')
       root.after(175, lambda: b12.config(bg = '#60eb85'))
    root.bind('<KeyPress-7>', flashb12)
    def flashb14(event):
       g14()
       b14.config(bg = 'green')
       root.after(175, lambda: b14.config(bg = '#60eb85'))
    root.bind('<KeyPress-8>', flashb14)
    def flashb16(event):
       g16()
       b16.config(bg = 'green')
       root.after(175, lambda: b16.config(bg = '#60eb85'))
    root.bind('<KeyPress-9>', flashb16)
    def flashb17(event):
       g17()
       b17.config(bg = 'green')
       root.after(175, lambda: b17.config(bg = '#60eb85'))
    root.bind('<KeyPress-0>', flashb17)
    def flashb19(event):
       g19()
       b19.config(bg = 'green')
       root.after(175, lambda: b19.config(bg = '#60eb85'))
    root.bind('<KeyPress-q>', flashb19)
    def flashb21(event):
       g21()
       b21.config(bg = 'green')
       root.after(175, lambda: b21.config(bg = '#60eb85'))
    root.bind('<KeyPress-w>', flashb21)
    def flashb23(event):
       g23()
       b23.config(bg = 'green')
       root.after(175, lambda: b23.config(bg = '#60eb85'))
    root.bind('<KeyPress-e>', flashb23)
    def flashb24(event):
       g24()
       b24.config(bg = 'green')
       root.after(175, lambda: b24.config(bg = '#60eb85'))
    root.bind('<KeyPress-r>', flashb24)
    def flashb26(event):
       g26()
       b26.config(bg = 'green')
       root.after(175, lambda: b26.config(bg = '#60eb85'))
    root.bind('<KeyPress-t>', flashb26)
    def flashb28(event):
       g28()
       b28.config(bg = 'green')
       root.after(175, lambda: b28.config(bg = '#60eb85'))
    root.bind('<KeyPress-y>', flashb28)
    def flashb29(event):
       g29()
       b29.config(bg = 'green')
       root.after(175, lambda: b29.config(bg = '#60eb85'))
    root.bind('<KeyPress-u>', flashb29)
    def flashb31(event):
       g31()
       b31.config(bg = 'green')
       root.after(175, lambda: b31.config(bg = '#60eb85'))
    root.bind('<KeyPress-i>', flashb31)
    def flashb33(event):
       g33()
       b33.config(bg = 'green')
       root.after(175, lambda: b33.config(bg = '#60eb85'))
    root.bind('<KeyPress-o>', flashb33)
    def flashb35(event):
       g35()
       b35.config(bg = 'green')
       root.after(175, lambda: b35.config(bg = '#60eb85'))
    root.bind('<KeyPress-p>', flashb35)
    def flashb36(event):
       g36()
       b36.config(bg = 'green')
       root.after(175, lambda: b36.config(bg = '#60eb85'))
    root.bind('<KeyPress-a>', flashb36)
    def flashb38(event):
       g38()
       b38.config(bg = 'green')
       root.after(175, lambda: b38.config(bg = '#60eb85'))
    root.bind('<KeyPress-s>', flashb38)
    def flashb40(event):
       g40()
       b40.config(bg = 'green')
       root.after(175, lambda: b40.config(bg = '#60eb85'))
    root.bind('<KeyPress-d>', flashb40)
    def flashb41(event):
       g41()
       b41.config(bg = 'green')
       root.after(175, lambda: b41.config(bg = '#60eb85'))
    root.bind('<KeyPress-f>', flashb41)
    def flashb43(event):
       g43()
       b43.config(bg = 'green')
       root.after(175, lambda: b43.config(bg = '#60eb85'))
    root.bind('<KeyPress-g>', flashb43)
    def flashb45(event):
       g45()
       b45.config(bg = 'green')
       root.after(175, lambda: b45.config(bg = '#60eb85'))
    root.bind('<KeyPress-h>', flashb45)
    def flashb47(event):
       g47()
       b47.config(bg = 'green')
       root.after(175, lambda: b47.config(bg = '#60eb85'))
    root.bind('<KeyPress-j>', flashb47)
    def flashb48(event):
       g48()
       b48.config(bg = 'green')
       root.after(175, lambda: b48.config(bg = '#60eb85'))
    root.bind('<KeyPress-k>', flashb48)
    def flashb50(event):
       g50()
       b50.config(bg = 'green')
       root.after(175, lambda: b50.config(bg = '#60eb85'))
    root.bind('<KeyPress-l>', flashb50)
    def flashb52(event):
       g52()
       b52.config(bg = 'green')
       root.after(175, lambda: b52.config(bg = '#60eb85'))
    root.bind('<KeyPress-z>', flashb52)
    def flashb53(event):
       g53()
       b53.config(bg = 'green')
       root.after(175, lambda: b53.config(bg = '#60eb85'))
    root.bind('<KeyPress-x>', flashb53)
    def flashb55(event):
       g55()
       b55.config(bg = 'green')
       root.after(175, lambda: b55.config(bg = '#60eb85'))
    root.bind('<KeyPress-c>', flashb55)
    def flashb57(event):
       g57()
       b57.config(bg = 'green')
       root.after(175, lambda: b57.config(bg = '#60eb85'))
    root.bind('<KeyPress-v>', flashb57)
    def flashb59(event):
       g59()
       b59.config(bg = 'green')
       root.after(175, lambda: b59.config(bg = '#60eb85'))
    root.bind('<KeyPress-b>', flashb59)
    def flashb60(event):
       g60()
       b60.config(bg = 'green')
       root.after(175, lambda: b60.config(bg = '#60eb85'))
    root.bind('<KeyPress-n>', flashb60)
    b2.configure(background='#60eb85',foreground='black')
    b4.configure(background='#60eb85',foreground='black')
    b5.configure(background='#60eb85')
    b7.configure(background='#60eb85',foreground='black')
    b9.configure(background='#60eb85',foreground='black')
    b11.configure(background='#60eb85',foreground='black')
    b12.configure(background='#60eb85')
    b14.configure(background='#60eb85',foreground='black')
    b16.configure(background='#60eb85',foreground='black')
    b17.configure(background='#60eb85')
    b19.configure(background='#60eb85',foreground='black')
    b21.configure(background='#60eb85',foreground='black')
    b23.configure(background='#60eb85',foreground='black')
    b24.configure(background='#60eb85')
    b26.configure(background='#60eb85',foreground='black')
    b28.configure(background='#60eb85',foreground='black')
    b29.configure(background='#60eb85')
    b31.configure(background='#60eb85',foreground='black')
    b33.configure(background='#60eb85',foreground='black')
    b35.configure(background='#60eb85',foreground='black')
    b36.configure(background='#60eb85')
    b38.configure(background='#60eb85',foreground='black')
    b40.configure(background='#60eb85',foreground='black')
    b41.configure(background='#60eb85')
    b43.configure(background='#60eb85',foreground='black')
    b45.configure(background='#60eb85',foreground='black')
    b47.configure(background='#60eb85',foreground='black')
    b48.configure(background='#60eb85')
    b50.configure(background='#60eb85',foreground='black')
    b52.configure(background='#60eb85',foreground='black')
    b53.configure(background='#60eb85')
    b55.configure(background='#60eb85',foreground='black')
    b57.configure(background='#60eb85',foreground='black')
    b59.configure(background='#60eb85',foreground='black')
    b60.configure(background='#60eb85')
def b_major_e3bcbd():
    b_b_h.place_forget()
    b_b.place(x=1100,y=50,width=80)
    b2.configure(background='black',foreground='white')
    b4.configure(background='black',foreground='white')
    b5.configure(background=orig_color)
    b7.configure(background='black',foreground='white')
    b9.configure(background='black',foreground='white')
    b11.configure(background='black',foreground='white')
    b12.configure(background=orig_color)
    b14.configure(background='black',foreground='white')
    b16.configure(background='black',foreground='white')
    b17.configure(background=orig_color)
    b19.configure(background='black',foreground='white')
    b21.configure(background='black',foreground='white')
    b23.configure(background='black',foreground='white')
    b24.configure(background=orig_color)
    b26.configure(background='black',foreground='white')
    b28.configure(background='black',foreground='white')
    b29.configure(background=orig_color)
    b31.configure(background='black',foreground='white')
    b33.configure(background='black',foreground='white')
    b35.configure(background='black',foreground='white')
    b36.configure(background=orig_color)
    b38.configure(background='black',foreground='white')
    b40.configure(background='black',foreground='white')
    b41.configure(background=orig_color)
    b43.configure(background='black',foreground='white')
    b45.configure(background='black',foreground='white')
    b47.configure(background='black',foreground='white')
    b48.configure(background=orig_color)
    b50.configure(background='black',foreground='white')
    b52.configure(background='black',foreground='white')
    b53.configure(background=orig_color)
    b55.configure(background='black',foreground='white')
    b57.configure(background='black',foreground='white')
    b59.configure(background='black',foreground='white')
    b60.configure(background=orig_color)
    ## Major Show and Hide Buttons###
b_c_h=Button(frame_major,text='C/Am',command=c_major_yellow,pady=10,background='yellow')
b_c_h.place(x=0,y=50,width=80)
b_c=Button(frame_major,text='C/Am',command=c_major_show,pady=10)
b_c.place(x=0,y=50,width=80)

b_c_sharp_h=Button(frame_major,text='C#/A#m',command=c_sharp_major_orange,pady=10,background='orange')
b_c_sharp_h.place(x=100,y=50,width=80)
b_c_sharp=Button(frame_major,text='C#/A#m',command=c_sharp_major_show,pady=10)
b_c_sharp.place(x=100,y=50,width=80)

b_d_h=Button(frame_major,text='D/Bm',command=d_major_e64040,pady=10,background='#41d95f')
b_d_h.place(x=200,y=50,width=80)
b_d=Button(frame_major,text='D/Bm',command=d_major_show,pady=10)
b_d.place(x=200,y=50,width=80)

b_d_sharp_h=Button(frame_major,text='D#/Cm',command=d_sharp_major_6fedd0,pady=10,background='#6fedd0')
b_d_sharp_h.place(x=300,y=50,width=80)
b_d_sharp=Button(frame_major,text='D#/Cm',command=d_sharp_major_show,pady=10)
b_d_sharp.place(x=300,y=50,width=80)

b_e_h=Button(frame_major,text='E/C#m',command=e_major_e39ad8,pady=10,background='#e39ad8')
b_e_h.place(x=400,y=50,width=80)
b_e=Button(frame_major,text='E/C#m',command=e_major_show,pady=10)
b_e.place(x=400,y=50,width=80)

b_f_h=Button(frame_major,text='F/Dm',command=f_major_ffc830,pady=10,background='#ffc830')
b_f_h.place(x=500,y=50,width=80)
b_f=Button(frame_major,text='F/Dm',command=f_major_show,pady=10)
b_f.place(x=500,y=50,width=80)

b_f_sharp_h=Button(frame_major,text='F#/D#m',command=f_sharp_major_f7929a,pady=10,background='#f5f071')
b_f_sharp_h.place(x=600,y=50,width=80)
b_f_sharp=Button(frame_major,text='F#/D#m',command=f_sharp_major_show,pady=10)
b_f_sharp.place(x=600,y=50,width=80)

b_g_h=Button(frame_major,text='G/Em',command=g_major_a8edaf,pady=10,background='#a8edaf')
b_g_h.place(x=700,y=50,width=80)
b_g=Button(frame_major,text='G/Em',command=g_major_show,pady=10)
b_g.place(x=700,y=50,width=80)

b_g_sharp_h=Button(frame_major,text='G#/Fm',command=g_sharp_major_d9a49a,pady=10,background='#90b5f0')
b_g_sharp_h.place(x=800,y=50,width=80)
b_g_sharp=Button(frame_major,text='G#/Fm',command=g_sharp_major_show,pady=10)
b_g_sharp.place(x=800,y=50,width=80)

b_a_h=Button(frame_major,text='A/F#m',command=a_major_e6d375,pady=10,background='#e6d375')
b_a_h.place(x=900,y=50,width=80)
b_a=Button(frame_major,text='A/F#m',command=a_major_show,pady=10)
b_a.place(x=900,y=50,width=80)

b_a_sharp_h=Button(frame_major,text='A#/Gm',command=a_sharp_major_a0eb38,pady=10,background='#a0eb38')
b_a_sharp_h.place(x=1000,y=50,width=80)
b_a_sharp=Button(frame_major,text='A#/Gm',command=a_sharp_major_show,pady=10)
b_a_sharp.place(x=1000,y=50,width=80)

b_b_h=Button(frame_major,text='B/G#m',command=b_major_e3bcbd,pady=10,background='#60eb85')
b_b_h.place(x=1100,y=50,width=80)
b_b=Button(frame_major,text='B/G#m',command=b_major_show,pady=10)
b_b.place(x=1100,y=50,width=80)
#################################FLAG FOR INSTRUMENT
#######################################################################
def g1():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(1).play(mixer.Sound('Audio/P1.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(1).play(mixer.Sound('Audio/P1.wav'))
def g2():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(2).play(mixer.Sound('Audio/P2.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(2).play(mixer.Sound('Audio/P2.wav'))
def g3():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(3).play(mixer.Sound('Audio/P3.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(3).play(mixer.Sound('Audio/P3.wav'))
def g4():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(4).play(mixer.Sound('Audio/P4.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(4).play(mixer.Sound('Audio/P4.wav'))
def g5():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(5).play(mixer.Sound('Audio/P5.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(5).play(mixer.Sound('Audio/P5.wav'))
def g6():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(6).play(mixer.Sound('Audio/P6.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(6).play(mixer.Sound('Audio/P6.wav'))
def g7():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(7).play(mixer.Sound('Audio/P7.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(7).play(mixer.Sound('Audio/P7.wav'))
def g8():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(8).play(mixer.Sound('Audio/P8.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(8).play(mixer.Sound('Audio/P8.wav'))
def g9():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(9).play(mixer.Sound('Audio/P9.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(9).play(mixer.Sound('Audio/P9.wav'))
def g10():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(10).play(mixer.Sound('Audio/P10.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(10).play(mixer.Sound('Audio/P10.wav'))
def g11():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(11).play(mixer.Sound('Audio/P11.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(11).play(mixer.Sound('Audio/P11.wav'))
def g12():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(12).play(mixer.Sound('Audio/P12.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(12).play(mixer.Sound('Audio/P12.wav'))
def g13():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(13).play(mixer.Sound('Audio/P13.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(13).play(mixer.Sound('Audio/P13.wav'))
def g14():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(14).play(mixer.Sound('Audio/P14.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(14).play(mixer.Sound('Audio/P14.wav'))
def g15():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(15).play(mixer.Sound('Audio/P15.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(15).play(mixer.Sound('Audio/P15.wav'))
def g16():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(16).play(mixer.Sound('Audio/P16.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(16).play(mixer.Sound('Audio/P16.wav'))
def g17():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(17).play(mixer.Sound('Audio/P17.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(17).play(mixer.Sound('Audio/P17.wav'))
def g18():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(18).play(mixer.Sound('Audio/P18.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(18).play(mixer.Sound('Audio/P18.wav'))
def g19():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(19).play(mixer.Sound('Audio/P19.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(19).play(mixer.Sound('Audio/P19.wav'))
def g20():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(20).play(mixer.Sound('Audio/P20.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(20).play(mixer.Sound('Audio/P20.wav'))
def g21():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(21).play(mixer.Sound('Audio/P21.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(21).play(mixer.Sound('Audio/P21.wav'))
def g22():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(22).play(mixer.Sound('Audio/P22.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(22).play(mixer.Sound('Audio/P22.wav'))
def g23():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(23).play(mixer.Sound('Audio/P23.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(23).play(mixer.Sound('Audio/P23.wav'))
def g24():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(24).play(mixer.Sound('Audio/P24.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(24).play(mixer.Sound('Audio/P24.wav'))
def g25():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(25).play(mixer.Sound('Audio/P25.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(25).play(mixer.Sound('Audio/P25.wav'))
def g26():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(26).play(mixer.Sound('Audio/P26.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(26).play(mixer.Sound('Audio/P26.wav'))
def g27():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(27).play(mixer.Sound('Audio/P27.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(27).play(mixer.Sound('Audio/P27.wav'))
def g28():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(28).play(mixer.Sound('Audio/P28.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(28).play(mixer.Sound('Audio/P28.wav'))
def g29():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(29).play(mixer.Sound('Audio/P29.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(29).play(mixer.Sound('Audio/P29.wav'))
def g30():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(30).play(mixer.Sound('Audio/P30.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(30).play(mixer.Sound('Audio/P30.wav'))
def g31():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(31).play(mixer.Sound('Audio/P31.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(31).play(mixer.Sound('Audio/P31.wav'))
def g32():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(32).play(mixer.Sound('Audio/P32.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(32).play(mixer.Sound('Audio/P32.wav'))
def g33():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(33).play(mixer.Sound('Audio/P33.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(33).play(mixer.Sound('Audio/P33.wav'))
def g34():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(34).play(mixer.Sound('Audio/P34.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(34).play(mixer.Sound('Audio/P34.wav'))
def g35():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(35).play(mixer.Sound('Audio/P35.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(35).play(mixer.Sound('Audio/P35.wav'))
def g36():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(36).play(mixer.Sound('Audio/P36.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(36).play(mixer.Sound('Audio/P36.wav'))
def g37():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(37).play(mixer.Sound('Audio/P37.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(37).play(mixer.Sound('Audio/P37.wav'))
def g38():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(38).play(mixer.Sound('Audio/P38.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(38).play(mixer.Sound('Audio/P38.wav'))
def g39():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(39).play(mixer.Sound('Audio/P39.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(39).play(mixer.Sound('Audio/P39.wav'))
def g40():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(40).play(mixer.Sound('Audio/P40.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(40).play(mixer.Sound('Audio/P40.wav'))
def g41():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(41).play(mixer.Sound('Audio/P41.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(41).play(mixer.Sound('Audio/P41.wav'))
def g42():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(42).play(mixer.Sound('Audio/P42.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(42).play(mixer.Sound('Audio/P42.wav'))
def g43():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(43).play(mixer.Sound('Audio/P43.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(43).play(mixer.Sound('Audio/P43.wav'))
def g44():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(44).play(mixer.Sound('Audio/P44.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(44).play(mixer.Sound('Audio/P44.wav'))
def g45():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(45).play(mixer.Sound('Audio/P45.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(45).play(mixer.Sound('Audio/P45.wav'))
def g46():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(46).play(mixer.Sound('Audio/P46.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(46).play(mixer.Sound('Audio/P46.wav'))
def g47():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(47).play(mixer.Sound('Audio/P47.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(47).play(mixer.Sound('Audio/P47.wav'))
def g48():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(48).play(mixer.Sound('Audio/P48.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(48).play(mixer.Sound('Audio/P48.wav'))
def g49():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(49).play(mixer.Sound('Audio/P49.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(49).play(mixer.Sound('Audio/P49.wav'))
def g50():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(50).play(mixer.Sound('Audio/P50.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(50).play(mixer.Sound('Audio/P50.wav'))
def g51():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(51).play(mixer.Sound('Audio/P51.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(51).play(mixer.Sound('Audio/P51.wav'))
def g52():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(52).play(mixer.Sound('Audio/P52.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(52).play(mixer.Sound('Audio/P52.wav'))
def g53():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(53).play(mixer.Sound('Audio/P53.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(53).play(mixer.Sound('Audio/P53.wav'))
def g54():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(54).play(mixer.Sound('Audio/P54.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(54).play(mixer.Sound('Audio/P54.wav'))
def g55():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(55).play(mixer.Sound('Audio/P55.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(55).play(mixer.Sound('Audio/P55.wav'))
def g56():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(56).play(mixer.Sound('Audio/P56.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(56).play(mixer.Sound('Audio/P56.wav'))
def g57():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(57).play(mixer.Sound('Audio/P57.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(57).play(mixer.Sound('Audio/P57.wav'))
def g58():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(58).play(mixer.Sound('Audio/P58.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(58).play(mixer.Sound('Audio/P58.wav'))
def g59():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(59).play(mixer.Sound('Audio/P59.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(59).play(mixer.Sound('Audio/P59.wav'))
def g60():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(60).play(mixer.Sound('Audio/P60.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(60).play(mixer.Sound('Audio/P60.wav'))
def g61():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(61).play(mixer.Sound('Audio/P61.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(61).play(mixer.Sound('Audio/P61.wav'))
#####################################PIANO KEYS
b1=Button(main_frame,text='C',background='white',command=g1)
b1.place(x=30,y=300,width=30,height=140)
b2=Button(main_frame,text='C#/Db',wraplength=20,justify=LEFT,background='black',foreground='white',command=g2)
b2.place(x=60,y=300,width=30,height=100)
b3=Button(main_frame,text='D',background='white',command=g3)
b3.place(x=90,y=300,width=30,height=140)
b4=Button(main_frame,text='D#/Eb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g4)
b4.place(x=120,y=300,width=30,height=100)
b5=Button(main_frame,text='E',background='white',command=g5)
b5.place(x=150,y=300,width=30,height=140)
b6=Button(main_frame,text='F',background='white',command=g6)
b6.place(x=180,y=300,width=30,height=140)
b7=Button(main_frame,text='F#/Gb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g7)
b7.place(x=210,y=300,width=30,height=100)
b8=Button(main_frame,text='G',background='white',command=g8)
b8.place(x=240,y=300,width=30,height=140)
b9=Button(main_frame,text='G#/Ab',wraplength=20,justify=LEFT,background='black',foreground='white',command=g9)
b9.place(x=270,y=300,width=30,height=100)
b10=Button(main_frame,text='A',background='white',command=g10)
b10.place(x=300,y=300,width=30,height=140)
b11=Button(main_frame,text='A#/Bb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g11)
b11.place(x=330,y=300,width=30,height=100)
b12=Button(main_frame,text='B',background='white',command=g12)
b12.place(x=360,y=300,width=30,height=140)
b13=Button(main_frame,text='C',background='white',command=g13)
b13.place(x=390,y=300,width=30,height=140)
b14=Button(main_frame,text='C#/Db',wraplength=20,justify=LEFT,background='black',foreground='white',command=g14)
b14.place(x=420,y=300,width=30,height=100)
b15=Button(main_frame,text='D',background='white',command=g15)
b15.place(x=450,y=300,width=30,height=140)
b16=Button(main_frame,text='D#/Eb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g16)
b16.place(x=480,y=300,width=30,height=100)
b17=Button(main_frame,text='E',background='white',command=g17)
b17.place(x=510,y=300,width=30,height=140)
b18=Button(main_frame,text='F',background='white',command=g18)
b18.place(x=540,y=300,width=30,height=140)
b19=Button(main_frame,text='F#/Gb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g19)
b19.place(x=570,y=300,width=30,height=100)
b20=Button(main_frame,text='G',background='white',command=g20)
b20.place(x=600,y=300,width=30,height=140)
b21=Button(main_frame,text='G#/Ab',wraplength=20,justify=LEFT,background='black',foreground='white',command=g21)
b21.place(x=630,y=300,width=30,height=100)
b22=Button(main_frame,text='A',background='white',command=g22)
b22.place(x=660,y=300,width=30,height=140)
b23=Button(main_frame,text='A#/Bb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g23)
b23.place(x=690,y=300,width=30,height=100)
b24=Button(main_frame,text='B',background='white',command=g24)
b24.place(x=720,y=300,width=30,height=140)
b25=Button(main_frame,text='C',background='white',command=g25)
b25.place(x=750,y=300,width=30,height=140)
b26=Button(main_frame,text='C#/Db',wraplength=20,justify=LEFT,background='black',foreground='white',command=g26)
b26.place(x=780,y=300,width=30,height=100)
b27=Button(main_frame,text='D',background='white',command=g27)
b27.place(x=810,y=300,width=30,height=140)
b28=Button(main_frame,text='D#/Eb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g28)
b28.place(x=840,y=300,width=30,height=100)
b29=Button(main_frame,text='E',background='white',command=g29)
b29.place(x=870,y=300,width=30,height=140)
b30=Button(main_frame,text='F',background='white',command=g30)
b30.place(x=900,y=300,width=30,height=140)
b31=Button(main_frame,text='F#/Gb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g31)
b31.place(x=930,y=300,width=30,height=100)
b32=Button(main_frame,text='G',background='white',command=g32)
b32.place(x=960,y=300,width=30,height=140)
b33=Button(main_frame,text='G#/Ab',wraplength=20,justify=LEFT,background='black',foreground='white',command=g33)
b33.place(x=990,y=300,width=30,height=100)
b34=Button(main_frame,text='A',background='white',command=g34)
b34.place(x=1020,y=300,width=30,height=140)
b35=Button(main_frame,text='A#/Bb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g35)
b35.place(x=1050,y=300,width=30,height=100)
b36=Button(main_frame,text='B',background='white',command=g36)
b36.place(x=1080,y=300,width=30,height=140)
b37=Button(main_frame,text='C',background='white',command=g37)
b37.place(x=1110,y=300,width=30,height=140)
b38=Button(main_frame,text='C#/Db',wraplength=20,justify=LEFT,background='black',foreground='white',command=g38)
b38.place(x=30,y=450,width=30,height=100)
b39=Button(main_frame,text='D',background='white',command=g39)
b39.place(x=60,y=450,width=30,height=140)
b40=Button(main_frame,text='D#/Eb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g40)
b40.place(x=90,y=450,width=30,height=100)
b41=Button(main_frame,text='E',background='white',command=g41)
b41.place(x=120,y=450,width=30,height=140)
b42=Button(main_frame,text='F',background='white',command=g42)
b42.place(x=150,y=450,width=30,height=140)
b43=Button(main_frame,text='F#/Gb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g43)
b43.place(x=180,y=450,width=30,height=100)
b44=Button(main_frame,text='G',background='white',command=g44)
b44.place(x=210,y=450,width=30,height=140)
b45=Button(main_frame,text='G#/Ab',wraplength=20,justify=LEFT,background='black',foreground='white',command=g45)
b45.place(x=240,y=450,width=30,height=100)
b46=Button(main_frame,text='A',background='white',command=g46)
b46.place(x=270,y=450,width=30,height=140)
b47=Button(main_frame,text='A#/Bb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g47)
b47.place(x=300,y=450,width=30,height=100)
b48=Button(main_frame,text='B',background='white',command=g48)
b48.place(x=330,y=450,width=30,height=140)
b49=Button(main_frame,text='C',background='white',command=g49)
b49.place(x=360,y=450,width=30,height=140)
b50=Button(main_frame,text='C#/Db',wraplength=20,justify=LEFT,background='black',foreground='white',command=g50)
b50.place(x=390,y=450,width=30,height=100)
b51=Button(main_frame,text='D',background='white',command=g51)
b51.place(x=420,y=450,width=30,height=140)
b52=Button(main_frame,text='D#/Eb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g52)
b52.place(x=450,y=450,width=30,height=100)
b53=Button(main_frame,text='E',background='white',command=g53)
b53.place(x=480,y=450,width=30,height=140)
b54=Button(main_frame,text='F',background='white',command=g54)
b54.place(x=510,y=450,width=30,height=140)
b55=Button(main_frame,text='F#/Gb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g55)
b55.place(x=540,y=450,width=30,height=100)
b56=Button(main_frame,text='G',background='white',command=g56)
b56.place(x=570,y=450,width=30,height=140)
b57=Button(main_frame,text='G#/Ab',wraplength=20,justify=LEFT,background='black',foreground='white',command=g57)
b57.place(x=600,y=450,width=30,height=100)
b58=Button(main_frame,text='A',background='white',command=g58)
b58.place(x=630,y=450,width=30,height=140)
b59=Button(main_frame,text='A#/Bb',wraplength=20,justify=LEFT,background='black',foreground='white',command=g59)
b59.place(x=660,y=450,width=30,height=100)
b60=Button(main_frame,text='B',background='white',command=g60)
b60.place(x=690,y=450,width=30,height=140)
b61=Button(main_frame,text='C',background='white',command=g61)
b61.place(x=720,y=450,width=30,height=140)

################################################
guitarmode=Label(frame_chord,text='composer active',bg='blue')
guitarmode.place(x=1200,y=10,height=80,width=105)
#########################functions for flags FOR PLAYING STYLE#######
flag_for_guitar=0
def deactivatesinglemode():
    btn_for_single_mode.config(bg='green')
    btn_for_piano_mode.config(bg=orig_color)
def deactivatepianomode():
    btn_for_single_mode.config(bg=orig_color)
    btn_for_piano_mode.config(bg='green')
def singlemode():
    global flag_for_guitar
    flag_for_guitar=0
    guitarmode.config(text='composer active')
    deactivatepianomode()
def pianomode():
    global flag_for_guitar
    flag_for_guitar=1
    guitarmode.config(text='piano mode active')
    deactivatesinglemode()
#########################flags FOR PLAYING STYLE#######
btn_for_single_mode=Button(frame_chord,text='piano mode',command=pianomode)
btn_for_single_mode.place(x=1100,y=50,height=40,width=85)
btn_for_piano_mode=Button(frame_chord,text='composer',command=singlemode)
btn_for_piano_mode.place(x=1100,y=5,height=40,width=85)

