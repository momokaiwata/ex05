import math
import random
import sys
import pygame as pg
import time
from pygame.locals import *

pg.init()

WIDTH = 1600  #横
HIGHT = 900   #縦
txt_origin = ["攻撃","防御","魔法","回復","調教","逃走"] #攻撃名
HP = 50  #勇者の体力
MP = 10  #勇者の攻撃残量
ENE_HP = 10  #slimeの体力

attack_interval = 5 #攻撃の間隔
last_attack_time = 0 #攻撃時刻
me_defense = 5 #防御力
clock = pg.time.Clock()
timer_event = USEREVENT + 1
pg.time.set_timer(timer_event, 5000) #5秒ごとにイベント発生
is_defending = False #防御フラグ
is_mouse_pressed = False
ene_img = pg.image.load("./ex05/fig/ene.png")


class Button:  #クリックのクラス
    def __init__(self, x, y, width, height, color, hover_color, text, text_color, action, num):  
        """
        x = 
        y = 
        width = 
        height = 
        color = 
        hover_color = 範囲にマウスが来たら色が変わる
        text = 
        text_color = 
        action = 
        num = 辞書の
        """
        self.rect = pg.Rect(x, y, width, height) #矩形領域(left,top,width,height)
        self.color = color #色
        self.hover_color = hover_color # 『なんの変数なのかわからない』
        self.text = text #テキスト
        self.text_color = text_color #テキストの色
        self.action = action #『動き?攻撃?』
        self.num = num #『回数か？』

    def draw(self,scr): # draw関数
        pg.draw.rect(scr, self.color, self.rect) # 様々な図形を描画。「scr = screen」
        font = pg.font.SysFont("hg正楷書体pro", 50) # フォントとtextのサイズ
        text_surface = font.render(self.text, True, self.text_color) # テキストを描写
        text_rect = text_surface.get_rect(center=self.rect.center) # 『画像の位置か?』
        scr.blit(text_surface, text_rect) #　指定の位置に描画

    def handle_event(self, event): #『なんの関数だ??』
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #クリックされたら
            if self.rect.collidepoint(event.pos): #点が矩形の内側にあるかどうか     
                self.action(self.num)

class Bougyo:
    def __init__(self, _bougyo):
        self.bougyo=_bougyo

def calculate_damage(damage, defense): #ダメージ計算
        
        defense_diff = damage - defense
        if defense_diff < 0:
            defense_diff = 0
        return defense_diff

def action(i):
    p = ["攻撃","防御","魔法","回復","調教","逃走"]



    print(p[i])

    #防御押されたら
    global is_mouse_pressed
    is_mouse_pressed=False
    if(i == 1):
        is_mouse_pressed=True

def main():
    global WIDTH,HIGHT,txt_t,txt_origin
    bg_image = "./ex05/fig/back.png"
    pg.display.set_caption("RPG初期段階")
    screen = pg.display.set_mode((WIDTH, HIGHT))
    clock  = pg.time.Clock()
    bg_img = pg.image.load(bg_image)
    bg_img = pg.transform.scale(bg_img,(WIDTH,HIGHT))
    ene_img = pg.image.load("./ex05/fig/ene.png")
    ene_rct = ene_img.get_rect()
    win = pg.image.load("./ex05/fig/win.png")
    win = pg.transform.scale(win,(WIDTH/4,HIGHT/2))
    win2 = pg.transform.scale(win,(WIDTH-100,HIGHT/4))
    font1 = pg.font.SysFont("hg正楷書体pro", 100)
    font2 = pg.font.SysFont("hg正楷書体pro", 50)
    text = "野生のスライムが現れた"
    txt = []
    #text_surface1 = font2.render(f"HP:{HP} MP:{MP}", True, (255,255,255))#119行目に移動した。
    text_surface2 = font2.render(f"HP:{ENE_HP}", True, (255,255,255))
    attack_slime = pg.image.load("./ex05/fig/momoka.png")
    attack_slime = pg.transform.scale(attack_slime, (300, 200))

    for i,tx in enumerate(txt_origin): #インスタンス化
        if i%2==0:
            button = Button(125, 500+(i//2)*100, 100, 50, (50,50,50), (0,0,0), tx, (255,255,255), action, i)
        else:
            button = Button(275, 500+(i//2)*100, 100, 50, (50,50,50), (0,0,0), tx, (255,255,255), action, i)
        txt.append(button)
    global HP
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:return
            
            if event.type == timer_event: 
                if not is_mouse_pressed:
                    HP -= 3

            for button in txt:
                button.handle_event(event)
                if HP < 0:
                   HP = 0


        current_time = time.time() #ここからワイの実装
        attack_interval = 5 #攻撃の間隔
        last_attack_time = 0 #攻撃時刻
        keika_time = current_time - last_attack_time
        if  keika_time >= attack_interval: #スライムの攻撃
            attack_x = random.randint(0, WIDTH - ene_img.get_width())
            attack_y = random.randint(0, HIGHT - ene_img.get_width())
            last_attack_time = current_time
            time.sleep(0) #攻撃の速さ
        if HP == 0:
            break 
#        #ここまでがワイの実装
            

        screen.blit(bg_img,[0,0])
        screen.blit(ene_img,[WIDTH/2-ene_rct.width/2+100,HIGHT/2])
        screen.blit(win,[50,400])
        screen.blit(win2,[50,50])
        screen.blit(attack_slime,[attack_x,attack_y]) #ここもワイ
        x=200

        for chr in text:
            rendered_text = font1.render(chr, True, (255, 255, 255))
            text_width = rendered_text.get_width()
            screen.blit(rendered_text,[x,100])
            x += text_width
        for i in txt:
            i.draw(screen)
        text_surface1 = font2.render(f"HP:{HP} MP:{MP}", True, (255,255,255))#75行目のをここに移動した。
        screen.blit(text_surface1,[100,350])
        screen.blit(text_surface2,[WIDTH/2-ene_rct.width/2+225,HIGHT/2-50])
        pg.display.update()
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()