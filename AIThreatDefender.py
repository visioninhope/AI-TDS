import os
import sys
import threading
import time
import warnings

import flet as ft

from Portscan_final import runner as runner
from other_python_files import PE_file_extraction as PE_file_extraction
from other_python_files import RunModel_1 as RunModel_1
from other_python_files import combinatrix2a as combinatrix2a
from other_python_files import wifi_detect as wifi_detect

current_dir = os.path.dirname(os.path.abspath(__file__))

other_python_files_path = os.path.join(current_dir, 'other_python_files')
sys.path.append(other_python_files_path)

Analysing_condition = True

warnings.filterwarnings("ignore")
global file_locations
global pop_message
global predict


def main(page: ft.Page):
    page.title = "AI Threat Defender"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_min_width = 500
    page.window_min_height = 500
    page.window_center = True
    dir = os.getcwd()
    copy = dir
    for i in range(len(copy)):
        if copy[i] == "/" and copy[i + 1] == "/":
            dir += "//"
            break
        elif copy[i] == "\\" and copy[i + 1] == "\\":
            dir += "\\\\"
            break
        elif copy[i] == "/" and copy[i + 1] != "/":
            dir += "/"
            break
        elif copy[i] == "\\" and copy[i + 1] != "\\":
            dir += "\\"
            break

    virus = []
    virus_dic = {}

    def delete_virus(e):
        for i in cl.controls:
            if i.value:
                virus.append(virus_dic[i.label])
            else:
                continue

        if virus:
            for i in virus:
                os.remove(i)

            popup_container_1.width = 600
            popup_container_1.height = 230
            popup_container_1.bgcolor = "green24"
            popup_container_1.content = ft.Container(
                ft.Text("""Congratulations! Your system is now secure.\n(Name of application) has successfully 
                detected and removed a potential threat from your computer.\nYour safety and privacy are our top 
                priorities.\nIf you have any further concerns or questions, feel free to contact our support 
                team.\nThank you for using (Name of application) to keep your system protected!
                        """, weight=ft.FontWeight.W_600, size=15),
                width=600,
                height=230,
            )

        else:
            popup_container_1.width = 400
            popup_container_1.height = 200
            popup_container_1.bgcolor = "red24"
            popup_container_1.content = ft.Container(
                ft.Text("""No Files Selected\nVirus is still in your system!
                        """, weight=ft.FontWeight.W_700, size=15, text_align='center'),
                width=600,
                height=230,
                alignment=ft.alignment.center
            )

        page.update()
        time.sleep(5)
        virus.clear()
        cl.controls.clear()
        popup_container_1.height = 0
        popup_container_1.width = 230
        page.update()
        time.sleep(1)
        inside_scan.height = 230
        j = 0.1
        for i in range(10):
            scan_animation_button.opacity = j
            page.update()
            j += 0.1
            time.sleep(0.10)
        page.update()

    def delete_file(e):

        if cl_2.controls[0].value:
            virus.append(virus_dic[cl_2.controls[0].label])

        if virus:
            for i in virus:
                os.remove(i)
            popup_container_2.width = 600
            popup_container_2.height = 230
            popup_container_2.bgcolor = "green24"
            popup_container_2.content = ft.Container(
                ft.Column(controls=[
                    ft.Text("""𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬! 𝗬𝗼𝘂𝗿 𝘀𝘆𝘀𝘁𝗲𝗺 𝗶𝘀 𝗻𝗼𝘄 𝘀𝗲𝗰𝘂𝗿𝗲.\n\n(
                    Name of application) has successfully detected and removed a potential threat from your 
                    computer.\n\nYour safety and privacy are our top priorities.\nIf you have any further concerns or 
                    questions, feel free to contact our support team.\n\nThank you for using (𝗡𝗮𝗺𝗲 𝗼𝗳 
                    𝗮𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻) to keep your system protected!
                            """, weight=ft.FontWeight.W_500, size=19),
                ], scroll=ft.ScrollMode.ALWAYS, expand=True),
                width=600,
                height=400,
                alignment=ft.alignment.center,

            )
            page.update()
            time.sleep(2)

        else:
            print()
            print(virus)
            print()
            popup_container_2.width = 600
            popup_container_2.height = 230
            file_main_image.height = 0
            popup_container_2.bgcolor = "red24"
            popup_container_2.content = ft.Container(
                ft.Text("""No Files Selected\nVirus is still in your system!
                        """, weight=ft.FontWeight.W_700, size=15, text_align="center"),
                width=600,
                height=230,
                alignment=ft.alignment.center
            )
            page.update()

        time.sleep(3)
        popup_container_2.height = 0

        popup_container_2.width = 400

        page.update()

        popup_container_2.expand = False

        popup_container_2.height = 0
        time.sleep(0.7)
        file_main_image.height = 50
        file_select_button.opacity = 100
        upload_button.opacity = 100
        file_content.height = 570
        file_content.expand = True
        virus.clear()
        cl_2.controls.clear()
        page.update()

    def stay_virus(e):
        popup_container_1.height = 0
        popup_container_1.width = 230
        page.update()
        time.sleep(0.9)
        inside_scan.height = 230
        j = 0.1
        virus.clear()
        cl.controls.clear()
        for i in range(10):
            scan_animation_button.opacity = j
            page.update()
            j += 0.1
            time.sleep(0.10)
        page.update()

    def stay_file(e):
        popup_container_2.width = 600
        popup_container_2.height = 230
        file_main_image.height = 0
        popup_container_2.bgcolor = "red24"
        popup_container_2.content = ft.Container(
            ft.Column(controls=[
                ft.Text("""        *Warning*         
                        """, weight=ft.FontWeight.W_900, size=30, text_align=ft.alignment.center),
                ft.Text("""   Virus is still in your system! 
                        """, weight=ft.FontWeight.W_500, size=20, text_align="center"),
            ], alignment=ft.MainAxisAlignment.CENTER
            ),
            width=600,
            height=230,
            alignment=ft.alignment.center
        )
        page.update()

        time.sleep(3)
        popup_container_2.height = 0
        file_main_image.height = 60
        popup_container_2.width = 500

        page.update()

        popup_container_2.expand = False

        popup_container_2.height = 0
        file_main_image.height = 60
        time.sleep(0.7)
        file_select_button.opacity = 100
        upload_button.opacity = 100
        file_content.height = 570
        file_content.expand = True
        virus.clear()
        cl_2.controls.clear()

        acc_model_1.value = "According to model 1 "
        acc_model_2.value = "According to model 2 "
        acc_model_3.value = "According to model 3 "
        acc_model_4.value = "According to model 4 "
        acc_model_5.value = "According to model 5 "
        acc_model_1.expand = True
        acc_model_2.expand = True
        acc_model_3.expand = True
        acc_model_4.expand = True
        acc_model_5.expand = True
        model_info_button_1.border_radius = 10
        model_info_button_2.border_radius = 10
        model_info_button_3.border_radius = 10
        model_info_button_4.border_radius = 10
        model_info_button_5.border_radius = 10
        model_info_button_1.margin = ft.margin.only(right=0)
        model_info_button_2.margin = ft.margin.only(right=0)
        model_info_button_3.margin = ft.margin.only(right=0)
        model_info_button_4.margin = ft.margin.only(right=0)
        model_info_button_5.margin = ft.margin.only(right=0)
        model_info_button_1.padding = 0
        model_info_button_2.padding = 0
        model_info_button_3.padding = 0
        model_info_button_4.padding = 0
        model_info_button_5.padding = 0
        page.update()

    cl = ft.Column(
        spacing=10,
        width=700,
        expand=True,
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.CENTER
    )

    cl_2 = ft.Column(
        spacing=10,
        width=700,
        expand=True,
        scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.CENTER
    )

    delete_button = ft.Container(ft.Column(controls=[

        ft.Container(ft.Row(controls=[ft.Container(width=5),
                                      ft.Text("Do you want to delete the \"Virus\" files", width=600, color="white",
                                              weight=ft.FontWeight.W_500)]), width=600),
        ft.Row(controls=[ft.ElevatedButton("Yes", on_click=delete_virus, color="Green", width=160),
                         ft.ElevatedButton("No", on_click=stay_virus, color="Red", width=160)],
               alignment=ft.MainAxisAlignment.SPACE_AROUND)], spacing=4, ),
        width=600, height=70, alignment=ft.alignment.center, blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
        bgcolor="white12", padding=5, border_radius=10
    )
    delete_button_2 = ft.Container(ft.Column(controls=[
        ft.Container(ft.Row(controls=[ft.Container(width=5),
                                      ft.Text("Do you want to Delete the \"Virus\" file", width=600, color="white",
                                              weight=ft.FontWeight.W_500)]), width=600),
        ft.Row(controls=[ft.ElevatedButton("Yes", on_click=delete_file, color="Green", width=160),
                         ft.ElevatedButton("No", on_click=stay_file, color="Red", width=160)],
               alignment=ft.MainAxisAlignment.SPACE_AROUND)], spacing=4, ),
        width=600, height=70, alignment=ft.alignment.center, blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
        bgcolor="white12", padding=5, border_radius=10
    )

    # File Picker

    def animate_popup_1():
        scan_animation_button.content = ft.Stack(controls=[scan_button])
        scan_button.content = scan_1
        scan_button.on_click = animate
        scan_button.alignment = ft.alignment.center
        scan_animation_button.opacity = 0
        page.update()

        if not cl:
            popup_container_1.bgcolor = "green"
            inside_scan.height = 0
            popup_container_1.content = ft.Text("CONGRATULATIONS, We didn't found any virus in this File")
            popup_container_1.height = 260
            popup_container_1.width = 600
            page.update()
            time.sleep(5)
            popup_container_1.height = 0
            popup_container_1.width = 230
            page.update()
            time.sleep(1)
            page.update()
            inside_scan.height = 230
            j = 0.1
            for i in range(10):
                scan_animation_button.opacity = j
                page.update()
                j += 0.1
                time.sleep(0.10)
            page.update()

        else:
            popup_container_1.bgcolor = "red"
            inside_scan.height = 0
            popup_container_1.content = ft.Column(controls=[
                ft.Container(
                    ft.Text("Virus has detected in your system", text_align="center", color="white", width=600),
                    width=600, border_radius=3, height=20), cl, delete_button
            ])
            popup_container_1.height = 350
            popup_container_1.width = 600
            page.update()

        page.update()

    # Pop 2
    acc_model_1 = ft.Text("According to model 1 ", expand=True, weight=ft.FontWeight.W_800)
    acc_model_2 = ft.Text("According to model 2 ", expand=True, weight=ft.FontWeight.W_800)
    acc_model_3 = ft.Text("According to model 3 ", expand=True, weight=ft.FontWeight.W_800)
    acc_model_4 = ft.Text("According to model 4 ", expand=True, weight=ft.FontWeight.W_800)
    acc_model_5 = ft.Text("According to model 5 ", expand=True, weight=ft.FontWeight.W_800)

    model_predict_info_1 = ft.Text("Click", color="#FF0000")
    model_predict_info_2 = ft.Text("Click", color="#FF0000")
    model_predict_info_3 = ft.Text("Click", color="#FF0000")
    model_predict_info_4 = ft.Text("Click", color="#FF0000")
    model_predict_info_5 = ft.Text("Click", color="#FF0000")

    def button_extend_1(e):
        model_info_button_1.height = 140 if model_info_button_1.height == 30 else 30
        model_info_button_1.width = 456 if model_info_button_1.width == 82 else 82
        model_info_button_1.update()

        if acc_model_1.value == "According to model 1 ":
            acc_model_1.value = ""
            acc_model_1.update()
            model_info_button_1.padding = 10
            model_info_button_1.update()
            time.sleep(0.5)
            acc_model_1.expand = False

        else:
            acc_model_1.expand = True
            acc_model_1.update()
            model_info_button_1.padding = 0
            model_info_button_1.update()
            time.sleep(0.3)
            acc_model_1.value = "According to model 1 "
        page.update()
        if model_predict_info_1.value == "Click":
            model_predict_info_1.value = ""
            model_info_button_1.border_radius = 10
            model_info_button_1.margin = ft.margin.only(right=20)
            length = len(predict[1])
            model_predict_info_1.padding = ft.padding.only(left=10)
            model_info_button_1.update()
            model_predict_info_1.update()
            k = ""
            for i in range(0, length):
                if model_predict_info_1.value != "Click":
                    k = k + predict[1][i]
                    model_predict_info_1.value = k
                    model_predict_info_1.update()
                    time.sleep(0.01)
                else:
                    break

        else:
            model_predict_info_1.value = ""
            model_info_button_1.border_radius = 50
            model_info_button_1.margin = ft.margin.only(right=0)
            model_predict_info_1.value = "Click"
            model_predict_info_1.padding = 0
            model_info_button_1.update()
            model_predict_info_1.update()

        page.update()

    def button_extend_2(e):

        model_info_button_2.height = 140 if model_info_button_2.height == 30 else 30
        model_info_button_2.width = 456 if model_info_button_2.width == 82 else 82
        model_info_button_2.update()

        if acc_model_2.value == "According to model 2 ":
            acc_model_2.value = ""
            acc_model_2.update()
            model_info_button_2.padding = 10
            model_info_button_2.update()
            time.sleep(0.5)
            acc_model_2.expand = False

        else:
            acc_model_2.expand = True
            acc_model_2.update()
            model_info_button_2.padding = 0
            model_info_button_2.update()
            time.sleep(0.3)
            acc_model_2.value = "According to model 2 "
        page.update()

        if model_predict_info_2.value == "Click":
            model_predict_info_2.value = ""
            model_info_button_2.border_radius = 10
            model_info_button_2.margin = ft.margin.only(right=20)
            length = len(predict[2])
            model_predict_info_2.padding = ft.padding.only(left=10)
            model_info_button_2.update()
            model_predict_info_2.update()
            k = ""
            for i in range(0, length):
                if model_predict_info_2.value != "Click":
                    k = k + predict[2][i]
                    model_predict_info_2.value = k
                    model_predict_info_2.update()
                    time.sleep(0.01)
                else:
                    break

        else:
            model_predict_info_2.value = ""
            model_info_button_2.border_radius = 50
            model_info_button_2.margin = ft.margin.only(right=0)
            model_predict_info_2.value = "Click"
            model_predict_info_2.padding = 0
            model_info_button_2.update()
            model_predict_info_2.update()
        page.update()

    def button_extend_3(e):

        model_info_button_3.height = 140 if model_info_button_3.height == 30 else 30
        model_info_button_3.width = 456 if model_info_button_3.width == 82 else 82
        model_info_button_3.update()

        if acc_model_3.value == "According to model 3 ":
            acc_model_3.value = ""
            acc_model_3.update()
            model_info_button_3.padding = 10
            model_info_button_3.update()
            time.sleep(0.5)
            acc_model_3.expand = False

        else:
            acc_model_3.expand = True
            acc_model_3.update()
            model_info_button_3.padding = 0
            model_info_button_3.update()
            time.sleep(0.3)
            acc_model_3.value = "According to model 3 "
        page.update()
        if model_predict_info_3.value == "Click":
            model_predict_info_3.value = ""
            model_info_button_3.border_radius = 10
            model_info_button_3.margin = ft.margin.only(right=20)
            length = len(predict[3])
            model_predict_info_3.padding = ft.padding.only(left=10)
            model_info_button_3.update()
            model_predict_info_3.update()
            k = ""
            for i in range(0, length):
                if model_predict_info_3.value != "Click":
                    k = k + predict[3][i]
                    model_predict_info_3.value = k
                    model_predict_info_3.update()
                    time.sleep(0.01)
                else:
                    break

        else:
            model_predict_info_3.value = ""
            model_info_button_3.border_radius = 50
            model_info_button_3.margin = ft.margin.only(right=0)
            model_predict_info_3.value = "Click"
            model_predict_info_3.padding = 0
            model_info_button_3.update()
            model_predict_info_3.update()

        page.update()

    def button_extend_4(e):

        model_info_button_4.height = 140 if model_info_button_4.height == 30 else 30
        model_info_button_4.width = 456 if model_info_button_4.width == 82 else 82

        model_info_button_4.update()

        if acc_model_4.value == "According to model 4 ":
            acc_model_4.value = ""
            acc_model_4.update()
            model_info_button_4.padding = 10
            model_info_button_4.update()
            time.sleep(0.5)
            acc_model_4.expand = False

        else:
            acc_model_4.expand = True
            acc_model_4.update()
            model_info_button_4.padding = 0
            model_info_button_4.update()
            time.sleep(0.3)
            acc_model_4.value = "According to model 4 "
        page.update()
        if model_predict_info_4.value == "Click":
            model_predict_info_4.value = ""
            model_info_button_4.border_radius = 10
            model_info_button_4.margin = ft.margin.only(right=20)
            length = len(predict[4])
            model_predict_info_4.padding = ft.padding.only(left=10)
            model_info_button_4.update()
            model_predict_info_4.update()
            k = ""
            for i in range(0, length):
                if model_predict_info_4.value != "Click":
                    k = k + predict[4][i]
                    model_predict_info_4.value = k
                    model_predict_info_4.update()
                    time.sleep(0.01)
                else:
                    break

        else:
            model_predict_info_4.value = ""
            model_info_button_4.border_radius = 50
            model_info_button_4.margin = ft.margin.only(right=0)
            model_predict_info_4.value = "Click"
            model_predict_info_4.padding = 0
            model_info_button_4.update()
            model_predict_info_4.update()

        page.update()

    def button_extend_5(e):

        model_info_button_5.height = 140 if model_info_button_5.height == 30 else 30
        model_info_button_5.width = 456 if model_info_button_5.width == 82 else 82
        model_info_button_5.update()

        if acc_model_5.value == "According to model 5 ":
            acc_model_5.value = ""
            acc_model_5.update()
            model_info_button_5.padding = 10
            model_info_button_5.update()
            time.sleep(0.5)
            acc_model_5.expand = False

        else:
            acc_model_5.expand = True
            acc_model_5.update()
            model_info_button_5.padding = 0
            model_info_button_5.update()
            time.sleep(0.3)
            acc_model_5.value = "According to model 5 "
        page.update()
        if model_predict_info_5.value == "Click":
            model_predict_info_5.value = ""
            model_info_button_5.border_radius = 10
            model_info_button_5.margin = ft.margin.only(right=20)
            length = len(predict[5])
            model_predict_info_5.padding = ft.padding.only(left=10)
            model_info_button_5.update()
            model_predict_info_5.update()
            k = ""
            for i in range(0, length):
                if model_predict_info_5.value != "Click":
                    k = k + predict[5][i]
                    model_predict_info_5.value = k
                    model_predict_info_5.update()
                    time.sleep(0.01)
                else:
                    break
        else:
            model_predict_info_5.value = ""
            model_info_button_5.border_radius = 50
            model_info_button_5.margin = ft.margin.only(right=0)
            model_predict_info_5.value = "Click"
            model_predict_info_5.padding = 0
            model_info_button_5.update()
            model_predict_info_5.update()
        page.update()

    model_info_button_1 = ft.Container(model_predict_info_1, on_click=button_extend_1, width=82, height=30,
                                       border_radius=50, bgcolor="#CCCCCC", alignment=ft.alignment.center,
                                       animate=ft.animation.Animation(300, "easeOut"))
    model_info_button_2 = ft.Container(model_predict_info_2, on_click=button_extend_2, width=82, height=30,
                                       border_radius=50, bgcolor="#CCCCCC", alignment=ft.alignment.center,
                                       animate=ft.animation.Animation(300, "easeOut"))
    model_info_button_3 = ft.Container(model_predict_info_3, on_click=button_extend_3, width=82, height=30,
                                       border_radius=50, bgcolor="#CCCCCC", alignment=ft.alignment.center,
                                       animate=ft.animation.Animation(300, "easeOut"))
    model_info_button_4 = ft.Container(model_predict_info_4, on_click=button_extend_4, width=82, height=30,
                                       border_radius=50, bgcolor="#CCCCCC", alignment=ft.alignment.center,
                                       animate=ft.animation.Animation(300, "easeOut"))
    model_info_button_5 = ft.Container(model_predict_info_5, on_click=button_extend_5, width=82, height=30,
                                       border_radius=50, bgcolor="#CCCCCC", alignment=ft.alignment.center,
                                       animate=ft.animation.Animation(300, "easeOut"))

    def animate_popup_2(predict, filelocation):
        global pop_message
        cl_2.controls.clear()

        model_info_button_1.height = 30
        model_info_button_1.width = 82

        model_info_button_2.height = 30
        model_info_button_2.width = 82

        model_info_button_3.height = 30
        model_info_button_3.width = 82

        model_info_button_4.height = 30
        model_info_button_4.width = 82

        model_info_button_5.height = 30
        model_info_button_5.width = 82

        model_predict_info_1.value = "Click"
        model_predict_info_2.value = "Click"
        model_predict_info_3.value = "Click"
        model_predict_info_4.value = "Click"
        model_predict_info_5.value = "Click"

        if predict[0] == 0:
            popup_container_2.bgcolor = "green"
            popup_container_2.height = 70
            file_main_image.height = 0
            popup_container_2.content = ft.Text("CONGRATULATIONS, We didn't Found any virus in this File")
            page.update()
            time.sleep(4)
            popup_container_2.height = 0
            file_main_image.height = 60
            page.update()

        elif predict[0] == 1:
            temp = filelocation
            temp1 = temp.split("/")
            virus_dic[temp1[-1]] = temp

            acc_model_1.color = "#2b2b2b"
            model_predict_info_1.color = "#2b2b2b"
            acc_model_2.color = "#2b2b2b"
            model_predict_info_2.color = "#2b2b2b"
            acc_model_3.color = "#2b2b2b"
            model_predict_info_3.color = "#2b2b2b"
            acc_model_4.color = "#2b2b2b"
            model_predict_info_4.color = "#2b2b2b"
            acc_model_5.color = "#2b2b2b"
            model_predict_info_5.color = "#2b2b2b"
            page.update()

            cl_2.controls.append(ft.Checkbox(label=temp1[-1], value=True))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_1, model_info_button_1])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_2, model_info_button_2])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_3, model_info_button_3])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_4, model_info_button_4])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_5, model_info_button_5])))
            popup_container_2.bgcolor = "#ebeb0c"
            popup_container_2.height = 570
            file_content.expand = False
            file_content.height = 0
            file_main_image.height = 0
            popup_container_2.content = ft.Column(controls=[
                ft.Container(ft.Text(
                    "Suspicious file : This might be a virus; inconclusive analysis by our models\n with the "
                    "slightest margins, indicates that it is a virus.",
                    text_align="center", color="#2b2b2b", width=600), width=600, border_radius=3, height=20), cl_2,
                delete_button_2,
            ])
            page.update()
            time.sleep(0.5)
            popup_container_2.expand = True
            file_select_button.opacity = 0
            upload_button.opacity = 0

        else:
            temp = filelocation
            temp1 = temp.split("/")
            virus_dic[temp1[-1]] = temp

            acc_model_1.color = "#fffcf5"
            acc_model_2.color = "#fffcf5"
            acc_model_3.color = "#fffcf5"
            acc_model_4.color = "#fffcf5"
            acc_model_5.color = "#fffcf5"

            cl_2.controls.append(ft.Checkbox(label=temp1[-1], value=True, check_color="black"))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_1, model_info_button_1])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_2, model_info_button_2])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_3, model_info_button_3])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_4, model_info_button_4])))
            cl_2.controls.append(ft.Container(ft.Row(controls=[ft.Container(ft.Text("    "), expand=True)]), height=2))
            cl_2.controls.append(ft.Container(ft.Row(controls=[acc_model_5, model_info_button_5])))
            popup_container_2.bgcolor = "red"
            popup_container_2.height = 570
            file_content.expand = False
            file_content.height = 0
            file_main_image.height = 0
            popup_container_2.content = ft.Column(controls=[
                ft.Container(ft.Text("Virus has detected in this File", text_align="center", color="white", width=600),
                             width=600, border_radius=3, height=20), cl_2, delete_button_2,
            ])
            page.update()
            time.sleep(0.5)
            popup_container_2.expand = True

            file_select_button.opacity = 0
            upload_button.opacity = 0

        page.update()

        # Pop 2-completed

    global file_locations
    file_locations = []

    def file_detect(e):
        upload_button.disabled = True
        upload_button.bgcolor = "#dddddd"
        upload_button.content.color = "black"
        upload_button.content = ft.Text("Loading...", text_align=ft.alignment.center, color="black")
        page.update()
        print()
        print(file_locations)

        predict = combinatrix2a.eng_predict(file_locations[0])
        animate_popup_2(predict, file_locations[0])
        upload_button.content = ft.Text("Upload", text_align=ft.alignment.center, color="black")
        page.update()
        file_locations.clear()

        # changes done here 2

    def dialog_picker(e: ft.FilePickerResultEvent):
        global file_locations
        if e.files is None:
            upload_button.disabled = True
            page.update()
        else:
            upload_button.disabled = False
            upload_button.bgcolor = "#4CAF50"
            upload_button.content.color = "#FFFFFF"
            page.update()
        for i in e.files:
            file_locations.append(i.path)
        page.update()

    pop_message = ft.Text()

    popup_container_1 = ft.Container(content=pop_message, width=230, height=0,
                                     animate=ft.animation.Animation(1000, "bounceOut"),
                                     alignment=ft.alignment.center,
                                     blur=5, bgcolor="green", padding=12)

    popup_container_2 = ft.Container(content=pop_message, width=500, height=0,
                                     animate=ft.animation.Animation(600, "bounceOut"),
                                     alignment=ft.alignment.center,
                                     blur=5, bgcolor="green", padding=12)
    file_picker = ft.FilePicker(on_result=dialog_picker)

    page.overlay.append(file_picker)  # It will pop up the file selection window without disturbing page layout
    page.update()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_f_png = os.path.join(current_dir, "images_proj\\file_f.png")

    file_select_button = ft.Container(content=ft.Row(controls=[
        ft.Container(ft.Image(src=file_f_png, width=30, height=30, fit=ft.ImageFit.CONTAIN), width=30, height=30,
                     margin=ft.margin.only(left=15)), ft.Text("Select a File", text_align=ft.alignment.center)]),
        on_click=lambda _: file_picker.pick_files(allow_multiple=True), height=40,
        width=180, bgcolor="#3498db", alignment=ft.alignment.center, border_radius=15,
        margin=ft.margin.only(left=170, right=170))

    file_upload = os.path.join(current_dir, "images_proj\\file_upload.png")
    upload_button = ft.Container(content=ft.Row(controls=[
        ft.Container(ft.Image(file_upload, width=40, height=40, fit=ft.ImageFit.CONTAIN), width=40, height=40,
                     margin=ft.margin.only(left=17)),
        ft.Text("Upload", text_align=ft.alignment.center, color="black")]), on_click=file_detect, height=40, width=180,
        disabled=True, bgcolor="#dddddd", alignment=ft.alignment.center, border_radius=15,
        margin=ft.margin.only(left=170, right=170))

    file_m_png = os.path.join(current_dir, "images_proj\\file_M.png")

    # changes done here
    file_image = url_image2 = ft.Container(ft.Image(src=file_m_png, width=300, height=250, fit=ft.ImageFit.CONTAIN),
                                           alignment=ft.alignment.center, width=300, height=250,
                                           margin=ft.margin.only(left=100, top=5, bottom=10))
    file_content = ft.Container(ft.Column(controls=[file_image, ft.Container(
        ft.Column(controls=[file_select_button, upload_button], spacing=10, width=500, height=100,
                  alignment=ft.MainAxisAlignment.CENTER), width=500, height=100, margin=ft.margin.only(bottom=100),
        alignment=ft.alignment.center)], alignment=ft.MainAxisAlignment.SPACE_EVENLY, width=500, height=1200,
                                          scroll=ft.ScrollMode.AUTO), width=500, height=600, expand=True,
                                alignment=ft.alignment.center, bgcolor="#4A6572", border_radius=10)

    file_text_png = os.path.join(current_dir, "images_proj\\file_text.png")
    file_main = ft.Container(ft.Image(src=file_text_png, width=80, height=100, fit=ft.ImageFit.CONTAIN), width=60,
                             height=100, margin=ft.margin.only(left=125, right=5))
    file_main_image = ft.Container(
        ft.Row(controls=[file_main, ft.Text("File Defender", text_align="center", size=35, weight=ft.FontWeight.W_500)]),
        alignment=ft.alignment.center_left, width=500, animate=ft.animation.Animation(600, "bounceOut"),
        height=63,
        bgcolor="#405762", border_radius=10)
    file_picker_content = ft.Container(
        ft.Column(controls=[popup_container_2,
                            file_main_image,
                            file_content
                            ]),
        expand=True,
        padding=ft.padding.only(top=30, bottom=30),
        alignment=ft.alignment.center,

    )

    # Thread 1
    global arg1
    arg1 = True

    # Create an event
    stop_event = threading.Event()

    def thread1():
        global arg1
        scan_bg.padding = 195
        while not stop_event.is_set():
            scan_bg.rotate.angle += 1
            page.update()
            time.sleep(0.07)

    # Thread 2
    global size
    global percentage
    global progress

    file_paths = PE_file_extraction.extract_file_paths()
    print(file_paths)

    def thread2():
        scan_button.disabled = True
        size = len(file_paths)

        percentage = 0
        progress = 1

        complete = 0

        while (percentage != 100):

            percentage = int((progress / size) * 100)

            num = ft.Text(percentage, size=30, weight=ft.FontWeight.W_900)
            predict = RunModel_1.predict_1(file_paths[complete])

            scan_button.content = ft.Container(
                ft.Stack(controls=[
                    ft.Container(
                        ft.Container(
                            width=300, height=300,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=[ft.colors.BLUE, ft.colors.BROWN],
                            ), shape=ft.BoxShape.CIRCLE, border_radius=200

                        ), alignment=ft.alignment.center
                    ),
                    ft.Container(
                        ft.Row(controls=[ft.Text(" ", size=5), num, ft.Text("%", size=40, weight=ft.FontWeight.W_900)],
                               alignment=ft.MainAxisAlignment.CENTER), alignment=ft.alignment.bottom_center,
                        padding=ft.padding.only(bottom=93)),

                ]),
                alignment=ft.alignment.bottom_left
            )
            progress = progress + 1

            page.update()

            if predict[0][0] == 1:
                print(file_paths[complete])
                predict2 = combinatrix2a.eng_predict(str(file_paths[complete]))
                if predict2[0] == 1:
                    temp = file_paths[complete]
                    temp1 = str(temp).split("/")
                    virus_dic[temp1[-1]] = temp

                    cl.controls.append(ft.Checkbox(label=temp1[-1], value=True))
            complete = complete + 1

            page.update()

        global arg1

        time.sleep(1)
        stop_event.set()
        animate_popup_1()
        scan_button.disabled = False
        page.update()

    def animate(e):
        scan_animation_button.content = ft.Stack(controls=[scan_bg, scan_button])
        page.update()
        threading.Thread(target=thread1).start()
        threading.Thread(target=thread2).start()

        page.update()

    scan_1 = ft.Container(ft.Stack(
        controls=[  # On start page scan 1st scan button
            ft.Container(
                ft.Container(  # Scan inside color
                    width=200, height=200,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.BLUE, ft.colors.BROWN],
                    ), shape=ft.BoxShape.CIRCLE, border_radius=180

                ), alignment=ft.alignment.center),
            ft.Container(
                ft.Text("SCAN", size=30, weight=ft.FontWeight.W_600), alignment=ft.alignment.center, padding=50)
        ]), alignment=ft.alignment.center
    )

    scan_button = ft.Container(

        scan_1, on_click=animate, alignment=ft.alignment.center
    )

    scan_bg = ft.Container(
        gradient=ft.SweepGradient(
            center=ft.alignment.center,
            colors=[
                "brown",
                "#C7206E9F86",
                "brown",

            ]),
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_IN_OUT),
        shape=ft.BoxShape.CIRCLE,
    )

    scan_animation_button = ft.Container(ft.Stack(controls=[scan_button]))

    inside_scan = ft.Container(scan_animation_button, width=230, height=230)
    scan = ft.Container(ft.Column(controls=[popup_container_1, inside_scan], alignment=ft.MainAxisAlignment.CENTER),
                        width=2000, height=1100, expand=True, alignment=ft.alignment.center)

    # Network page content

    def Analysing():
        global Analysing_condition
        a = "Analyzing"
        b = " Analyzing."
        c = "  Analyzing.."
        d = "   Analyzing..."
        e = "    Analyzing...."
        al = [a, b, c, d, e]
        i = 0
        network_analysis.bgcolor = "#dddddd"
        page.update()
        while Analysing_condition:
            network_analysis.content = ft.Text(al[i % 5], color="black")
            time.sleep(0.4)
            page.update()
            i += 1
        print("loop exited")
        network_analysis.content = ft.Text("Start Analysis", text_align=ft.alignment.center, color="black")
        network_analysis.bgcolor = "#dddddd"
        network_analysis.border_radius = 20
        page.update()
        time_1.value = ""
        network_analysis.margin = ft.margin.only(left=120, right=120)
        network_analysis.disabled = True
        network_analysis.padding = 0
        page.update()
        return

    def thread3():
        global num
        num = True
        while num:
            tan = 0
            while wifi_detect.check_and_print_wifi_status() != "connected" and num == True:
                popup_container_3.content = ft.Text("Wifi Not Connected")
                Network_heading.height = 0
                popup_container_3.height = 50
                popup_container_3.bgcolor = "red24"
                network_analysis.content = ft.Text("Start Analysis", text_align=ft.alignment.center, color="black")
                network_analysis.bgcolor = "#dddddd"
                network_analysis.alignment = ft.alignment.center
                network_analysis.border_radius = 20
                network_analysis.margin = ft.margin.only(left=120, right=120)
                network_analysis.disabled = True
                network_analysis.bgcolor = "#dddddd"
                page.update()
                page.update()
                tan = 1

            if tan == 1:
                popup_container_3.content = ft.Text("Wi-Fi Connected Please Re-Analysis")
                popup_container_3.height = 50
                Network_heading.height = 0
                popup_container_3.bgcolor = "green24"
                page.update()
                time_1.error_text = None
                time_1.helper_text = None
                network_analysis.content = ft.Text("Start Analysis", text_align=ft.alignment.center, color="black")
                network_analysis.bgcolor = "#dddddd"
                network_analysis.alignment = ft.alignment.center
                network_analysis.border_radius = 20
                network_analysis.margin = ft.margin.only(left=120, right=120)
                network_analysis.disabled = True
                network_analysis.bgcolor = "#dddddd"
                page.update()
                num = False
                global Analysing_condition
                Analysing_condition = False
                page.update()

        time.sleep(2)
        popup_container_3.height = 0
        page.update()
        Network_heading.height = 60
        print("hello 1")
        page.update()

    num = True

    # Wifi detect complete
    def network_check(e):

        global Analysing_condition
        time_1.error_text = None
        wifi_status = wifi_detect.check_and_print_wifi_status()
        if wifi_status == "connected":
            network_analysis.content = ft.Text("Analyzing", color="black", text_align="center")
            network_analysis.padding = ft.padding.only(right=18)
            network_analysis.alignment = ft.alignment.center
            threading.Thread(target=thread3).start()
            threading.Thread(target=Analysing).start()
            network = runner.network_run(time_1.value)

            global num
            num = False
            if network == 1:
                Network_heading.height = 0
                popup_container_3.height = 60
                pop_message.value = "A Port Scan has been attempted on your System"
                popup_container_3.bgcolor = "red24"
                popup_container_3.padding = 10
                page.update()
                time.sleep(30)
            elif network == 2:
                Network_heading.height = 0
                popup_container_3.height = 60
                pop_message.value = ("Mostly normal network activity, However Our AI/ML model suspects a small scale "
                                     "Port Scan activity in your Network")
                popup_container_3.padding = 10
                pop_message.color = "#333333"
                popup_container_3.bgcolor = "orange12"
                page.update()
                time.sleep(30)
            elif network == 3:
                Network_heading.height = 0
                popup_container_3.height = 60
                pop_message.value = "Perfectly normal network activity, Happy Networking!!"
                popup_container_3.bgcolor = "green24"
                popup_container_3.padding = 10
                page.update()
                time.sleep(30)
            Analysing_condition = False

            Network_heading.height = 60
            popup_container_3.height = 0
            popup_container_3.padding = 0
            page.update()
            pop_message.color = "white"
        else:
            while wifi_status != "connected":
                wifi_status = wifi_detect.check_and_print_wifi_status()
                popup_container_3.content = ft.Text("Wifi Not Connected")
                popup_container_3.height = 60
                Network_heading.height = 0
                popup_container_3.bgcolor = "red24"
                page.update()

            popup_container_3.content = ft.Text("Wifi Connected")
            popup_container_3.height = 60
            Network_heading.height = 0
            popup_container_3.bgcolor = "green24"
            page.update()
            time.sleep(3)
        page.update()
        popup_container_3.height = 0
        Network_heading.height = 60
        page.update()
        num = True

    # Network_predict=

    def network_button_enable(e):
        if time_1.value != "":
            try:
                time_1.error_text = None
                time_1.helper_text = None
                page.update()
                time_1.value = int(time_1.value)
                if time_1.value == "":
                    network_analysis.disabled = True
                    network_analysis.bgcolor = "#dddddd"
                    network_analysis.content = ft.Text("Start Analysis", text_align=ft.alignment.center, color="black")
                    network_analysis.alignment = ft.alignment.center
                    network_analysis.border_radius = 20
                    network_analysis.margin = ft.margin.only(left=120, right=120)
                    page.update()
                else:
                    if time_1.value >= 600:
                        time_1.helper_text = "Analysing may take time"
                        time_1.margin = ft.padding.only(top=5)
                    network_analysis.disabled = False
                    network_analysis.bgcolor = "green24"

                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    search_png = os.path.join(current_dir, "images_proj\\search.png")

                    network_upload_img = ft.Container(
                        ft.Image(src=search_png, width=30, height=40, fit=ft.ImageFit.CONTAIN), width=30, height=40,
                        margin=ft.margin.only(left=42))
                    network_analysis.content = ft.Row(controls=[network_upload_img, ft.Text("Start Analysis",
                                                                                            text_align=ft.alignment.center,
                                                                                            color="black")])
                    page.update()
            except:
                if time_1.value != "":
                    time_1.error_text = "Invalid Input"
                    network_analysis.disabled = True
                    network_analysis.bgcolor = "#dddddd"
                    network_analysis.bgcolor = "#dddddd"
                    network_analysis.content = ft.Text("Start Analysis", text_align=ft.alignment.center, color="black")
                    network_analysis.alignment = ft.alignment.center
                    network_analysis.border_radius = 20
                    network_analysis.margin = ft.margin.only(left=120, right=120)
                    page.update()
        else:
            time_1.error_text = None
            time_1.helper_text = None
            network_analysis.content = ft.Text("Start Analysis", text_align=ft.alignment.center, color="black")
            network_analysis.bgcolor = "#dddddd"
            network_analysis.alignment = ft.alignment.center
            network_analysis.border_radius = 20
            network_analysis.margin = ft.margin.only(left=120, right=120)
            network_analysis.disabled = True
            network_analysis.bgcolor = "#dddddd"
            page.update()
        global Analysing_condition
        Analysing_condition = True

    time_1 = ft.TextField(label="Enter Number of Seconds", hint_text="Enter Seconds", width=350, height=70,
                          border=False, on_change=network_button_enable, on_submit=network_check)
    time_input = ft.Container(time_1, width=350, height=60, alignment=ft.alignment.center,
                              margin=ft.margin.only(left=120, right=120))
    network_analysis = ft.Container(content=ft.Text("Start Analysis", text_align="left", color="black"), height=50,
                                    width=350, disabled=True, alignment=ft.alignment.center, on_click=network_check,
                                    border_radius=20, bgcolor="#dddddd", margin=ft.margin.only(left=120, right=120),
                                    animate=ft.animation.Animation(600,"bounceOut"))

    network_heading_png = os.path.join(current_dir, "images_proj\\network_heading.png")
    Network_image_M = url_image2 = ft.Container(
        ft.Image(src=network_heading_png, width=300, height=250, fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center, width=300, height=250, margin=ft.margin.only(left=100, top=5, bottom=10))
    network_container = ft.Container(ft.Column(controls=[Network_image_M, ft.Container(
        ft.Column(controls=[time_input, network_analysis], spacing=10, width=500, height=100,
                  alignment=ft.MainAxisAlignment.CENTER), width=500, height=100, margin=ft.margin.only(bottom=100),
        alignment=ft.alignment.center, )], alignment=ft.MainAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO),
                                     width=1980, height=1250, expand=True, alignment=ft.alignment.center,
                                     bgcolor="#4A6572", border_radius=10)

    popup_container_3 = ft.Container(content=pop_message, width=600, height=0,
                                     animate=ft.animation.Animation(600, "bounceOut"),
                                     alignment=ft.alignment.center,
                                     blur=5, bgcolor="green", padding=12)

    network_2_png = os.path.join(current_dir, "images_proj\\network_2.png")
    Network_heading_text = ft.Container(ft.Image(src=network_2_png, width=120, height=130, fit=ft.ImageFit.CONTAIN),
                                        width=130, height=130, margin=ft.margin.only(left=40))
    Network_heading = ft.Container(ft.Row(controls=[Network_heading_text,
                                                    ft.Text("Network Scan", text_align="center", size=35,
                                                            weight=ft.FontWeight.W_500)]),
                                   alignment=ft.alignment.center_left, width=1980, height=60, bgcolor="#405762",border_radius=10)

    Network = ft.Container(
        ft.Column(controls=[popup_container_3,
                            Network_heading,
                            network_container
                            ]),
        expand=True,
        padding=ft.padding.only(top=30, bottom=30),
        width=500,
        height=600,
        alignment=ft.alignment.center,
    )

    def url_detect(e):
        url_button.disabled = True
        url = 1
        if url == 1:
            Url_main_image.height = 0
            popup_container_4.height = 60
            pop_message.value = ("Your feedback has been successfully received. Thanks for helping us improve. We "
                                 "appreciate your valuable input")
            popup_container_4.bgcolor = "green24"
            popup_container_4.padding = 10
            page.update()
            url_button.bgcolor = "#dddddd"
            url_button.disabled = True
            page.update()
            from other_python_files import feedback as feedback
            feedback.email_feedback(input.value, "jhonel.alam@tup.edu.ph")

        time.sleep(30)
        Url_main_image.height = 60
        popup_container_4.height = 0
        popup_container_4.padding = 0
        page.update()

    def feedback_change(e):
        if input.value != "":
            url_button.bgcolor = "green24"
            url_button.disabled = False
            page.update()

        else:
            url_button.bgcolor = "#dddddd"
            url_button.disabled = True
            page.update()

    input = ft.TextField(label="Enter your comments here", width=350, expand=True, border=False,
                         on_change=feedback_change, multiline=True, min_lines=1,
                         max_lines=3, )
    url_input = ft.Container(input, width=350, height=80, alignment=ft.alignment.center,
                             margin=ft.margin.only(left=80, right=80), )
    url_button = ft.Container(content=ft.Text("Submit", text_align=ft.alignment.center, color="black"),
                              on_click=url_detect, height=40, width=350, disabled=True, bgcolor="#dddddd",
                              alignment=ft.alignment.center, border_radius=20,
                              margin=ft.margin.only(left=120, right=120))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    feedback_png = os.path.join(current_dir, "images_proj\\feedback.png")

    url_image = ft.Container(ft.Image(src=feedback_png, width=80, height=100, fit=ft.ImageFit.CONTAIN), width=60,
                             height=100, margin=ft.margin.only(left=100))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    url2_png = os.path.join(current_dir, "images_proj\\url2.png")

    url_image2 = ft.Container(ft.Image(src=url2_png, width=300, height=250, fit=ft.ImageFit.CONTAIN),
                              alignment=ft.alignment.center, width=300, height=250,
                              margin=ft.margin.only(left=120, top=20))

    URL_container = ft.Container(ft.Column(controls=[url_image2, ft.Container(
        ft.Column(controls=[url_input, url_button], spacing=10, width=550, height=150, ), width=550, height=150,
        margin=ft.margin.only(bottom=100))], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=600, height=1200,
                                           scroll=ft.ScrollMode.AUTO), width=1980, height=1250, expand=True,
                                 alignment=ft.alignment.center, bgcolor="#4A6572", border_radius=10)

    popup_container_4 = ft.Container(content=pop_message, width=600, height=0,
                                     animate=ft.animation.Animation(600, "bounceOut"),
                                     alignment=ft.alignment.center,
                                     blur=5, bgcolor="green", padding=12)

    Url_main_image = ft.Container(
        ft.Row(controls=[url_image, ft.Text("Evaluation", text_align="center", size=35, weight=ft.FontWeight.W_500)]),
        alignment=ft.alignment.center_left, width=1980, height=60, bgcolor="#405762", border_radius=10)
    URL = ft.Container(
        ft.Column(controls=[popup_container_4,
                            Url_main_image,
                            URL_container
                            ]),
        expand=True,
        padding=ft.padding.only(top=30, bottom=30),
        width=500,
        height=600,
        alignment=ft.alignment.center,
    )

    # Title bar

    page.appbar = ft.AppBar(
        center_title=True,
        toolbar_height=70,
        bgcolor="white",
        title=ft.Text("AI Threat Defender", color="red", size=40, weight=ft.FontWeight.W_500),
    )
    # Change Navigation

    def change_nav(e):
        if e.control.selected_index == 0:
            page.clean()
            page.add(
                scan
            )
        elif e.control.selected_index == 1:
            page.clean()
            page.add(
                file_picker_content
            )

        elif e.control.selected_index == 2:
            page.clean()
            page.add(
                Network
            )
        elif e.control.selected_index == 3:
            page.clean()
            page.add(
                URL
            )

    # Page navigation
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.SHIELD_OUTLINED,
                selected_icon=ft.icons.SHIELD,
                label="System Scan",
            ),
            ft.NavigationDestination(
                icon=ft.icons.SCREEN_SEARCH_DESKTOP_OUTLINED,
                selected_icon=ft.icons.SCREEN_SEARCH_DESKTOP_ROUNDED,
                label="Scan files",
            ),
            ft.NavigationDestination(
                icon=ft.icons.MONITOR_HEART_OUTLINED,
                selected_icon=ft.icons.MONITOR_HEART_ROUNDED,
                label="Network Scanning",
            ),
            ft.NavigationDestination(
                icon=ft.icons.FEEDBACK_OUTLINED,
                selected_icon=ft.icons.FEEDBACK_ROUNDED,
                label="Evaluation",
            )
        ],

        on_change=lambda e: change_nav(e),

    )

    # Page
    page.add(
        scan
    )
    page.bgcolor = "#344955"
    page.update()


ft.app(main, )
