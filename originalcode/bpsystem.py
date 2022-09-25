# bp system for FEG Identity V
from PySide6.QtWidgets import QApplication, QCompleter
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

strlstMap = ['军工厂jgc', '红教堂hjt', '圣心医院sxyy', '湖景村hjc',
             '月亮河公园ylhgy', '里奥的回忆ladhy', '永眠镇ymz', '唐人街trj']
dictMap = {'军工厂jgc': '军工厂', '红教堂hjt':'红教堂', '圣心医院sxyy':'圣心医院', '湖景村hjc':'湖景村',
             '月亮河公园ylhgy':'月亮河公园', '里奥的回忆ladhy':'里奥的回忆', '永眠镇ymz':'永眠镇', '唐人街trj':'唐人街'}
strlstSur = ['病患bh', '慈善家csj', '大副df', '古董商gds', '调酒师tjs', '调香师txs',
             '画家hj', '击球手jqs', '机械师jxs', '祭司js','教授js', '勘探员kty',
             '空军kj', '哭泣小丑kqxc', '昆虫学者kcxz', '律师ls', '盲女mn',
             '冒险家mxj', '魔术师mss', '牛仔nz', '前锋qf', '囚徒qt', '入殓师rls',
             '守墓人smr', '玩具商wjs', '舞女wn', '先知xz', '小女孩xnh',
             '小说家xsj', '心理学家xlxj', '幸运儿xye', '野人yr', '医生ys',
             '佣兵yb', '邮差yc', '园丁yd', '杂技演员zjyy', '咒术师zss']
dictSurName = {'病患bh':'病患', '慈善家csj':'“慈善家”', '大副df':'大副', '古董商gds':'古董商', '调酒师tjs':'调酒师', '调香师txs':'调香师',
             '画家hj':'画家', '击球手jqs':'击球手', '机械师jxs':'机械师', '祭司js':'祭司',
             '教授js':'教授', '勘探员kty':'勘探员',
             '空军kj':'空军', '哭泣小丑kqxc':'哭泣小丑', '昆虫学者kcxz':'昆虫学者', '律师ls':'律师', '盲女mn':'盲女',
             '冒险家mxj':'冒险家', '魔术师mss':'魔术师', '牛仔nz':'牛仔', '前锋qf':'前锋', '囚徒qt':'“囚徒”', '入殓师rls':'入殓师',
             '守墓人smr':'守墓人', '玩具商wjs':'玩具商', '舞女wn':'舞女', '先知xz':'先知', '小女孩xnh':'“小女孩”',
             '小说家xsj':'小说家', '心理学家xlxj':'“心理学家”', '幸运儿xye':'幸运儿', '野人yr':'野人', '医生ys':'医生',
             '佣兵yb':'佣兵', '邮差yc':'邮差', '园丁yd':'园丁', '杂技演员zjyy':'杂技演员', '咒术师zss':'咒术师'}
strlstHun = ['26号守卫26hsw', '爱哭鬼akg', '博士bs', '厂长cz', '雕刻家dkj',
             '噩梦em', '疯眼fy', '红蝶hd', '红夫人hfr', '黄衣之主hyzz',
             '杰克jk','记录员jly', '蜡像师lxs', '鹿头lt', '梦之女巫mznw', '孽蜥nx',
             '破轮pl', '摄影师sys', '使徒st', '宿伞之魂sszh', '小丑xc',
             '小提琴家xtqj', '渔女yn', '隐士ys', '蜘蛛zz']
dictHunName = {'26号守卫26hsw':'26号守卫', '爱哭鬼akg':'爱哭鬼', '博士bs':'“博士”', '厂长cz':'厂长', '雕刻家dkj':'雕刻家',
             '噩梦em':'“噩梦”', '疯眼fy':'疯眼', '红蝶hd':'红蝶', '红夫人hfr':'红夫人', '黄衣之主hyzz':'黄衣之主',
             '杰克jk':'“杰克”','记录员jly':'记录员', '蜡像师lxs':'蜡像师', '鹿头lt':'鹿头', '梦之女巫mznw':'梦之女巫', '孽蜥nx':'孽蜥',
             '破轮pl':'破轮', '摄影师sys':'摄影师', '使徒st':'“使徒”', '宿伞之魂sszh':'宿伞之魂', '小丑xc':'小丑',
             '小提琴家xtqj':'小提琴家', '渔女yn':'渔女', '隐士ys':'隐士', '蜘蛛zz':'蜘蛛'}

class claWinFg:
    def __init__(self):
        self.ui = QUiLoader().load('./ui/WinFg.ui')
        self.ui.setMaximumSize(1440, 810)
        self.ui.setMinimumSize(1440, 810)
        pix = QPixmap('./pic/background.png')
        pix = pix.scaled(self.ui.labBg.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labBg.setPixmap(pix)

    def updateSurBan1Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurBan1Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan1Pic.setPixmap(pix)

    def updateSurBan2Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurBan2Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan2Pic.setPixmap(pix)

    def updateSurBan3Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurBan3Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan3Pic.setPixmap(pix)

    def updateSurBan4Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurBan4Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan4Pic.setPixmap(pix)

    def updateSurBan5Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurBan5Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan5Pic.setPixmap(pix)

    def updateSurBan6Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurBan6Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan6Pic.setPixmap(pix)

    def updateHunBan1Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/hun/' + ss + '.png')
        pix = pix.scaled(self.ui.labHunBan1Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan1Pic.setPixmap(pix)

    def updateHunBan2Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/hun/' + ss + '.png')
        pix = pix.scaled(self.ui.labHunBan2Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan2Pic.setPixmap(pix)

    def updateHunBan3Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/hun/' + ss + '.png')
        pix = pix.scaled(self.ui.labHunBan3Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan3Pic.setPixmap(pix)

    def updateHunBan4Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/hun/' + ss + '.png')
        pix = pix.scaled(self.ui.labHunBan4Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan4Pic.setPixmap(pix)

    def updateSurPick1Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurPick1Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick1Pic.setPixmap(pix)
        self.ui.labSurPick1.setText(dictSurName[ss] if ss in strlstSur else '')

    def updateSurPick2Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurPick2Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick2Pic.setPixmap(pix)
        self.ui.labSurPick2.setText(dictSurName[ss] if ss in strlstSur else '')

    def updateSurPick3Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurPick3Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick3Pic.setPixmap(pix)
        self.ui.labSurPick3.setText(dictSurName[ss] if ss in strlstSur else '')

    def updateSurPick4Pic(self, ss):
        pix = QPixmap()
        pix.load('./pic/sur/' + ss + '.png')
        pix = pix.scaled(self.ui.labSurPick4Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick4Pic.setPixmap(pix)
        self.ui.labSurPick4.setText(dictSurName[ss] if ss in strlstSur else '')

    def updateHunPickPic(self, ss):
        pix = QPixmap()
        pix.load('./pic/hunBig/' + ss + '.png')
        # pix = pix.scaledToWidth(self.ui.labHunPickPic.width(), Qt.SmoothTransformation)
        pix = pix.scaled(self.ui.labHunPickPic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunPickPic.setPixmap(pix)
        self.ui.labHunPick.setText(dictHunName[ss] if ss in strlstHun else '')

    def updateSurTeam(self, ss):
        self.ui.labSurTeam.setText(ss)

    def updateHunTeam(self, ss):
        self.ui.labHunTeam.setText(ss)

    def updateMap(self, ss):
        pix = QPixmap()
        pix.load('./pic/map/' + ss + '.png')
        pix = pix.scaled(self.ui.labMapPic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labMapPic.setPixmap(pix)
        self.ui.labMap.setText(dictMap[ss] if ss in strlstMap else '')


class claWinBg:
    def __init__(self):
        self.ui = QUiLoader().load('./ui/WinBg.ui')

        # 交换队伍
        self.ui.pButSwapTeam.clicked.connect(self.swapTeam)

        # 重置
        self.ui.pBtnRes.clicked.connect(self.resetAll)

        # 地图选项卡
        self.ui.cBoxMap.addItems(['']+strlstMap)
        self.compMap = QCompleter(strlstMap)
        self.compMap.setFilterMode(Qt.MatchContains)
        self.ui.cBoxMap.setCompleter(self.compMap)

        # ban求生者
        self.ui.cBoxSurBan1.addItems(['']+strlstSur)
        self.compSurBan1 = QCompleter(strlstSur)
        self.compSurBan1.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurBan1.setCompleter(self.compSurBan1)

        self.ui.cBoxSurBan2.addItems(['']+strlstSur)
        self.compSurBan2 = QCompleter(strlstSur)
        self.compSurBan2.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurBan2.setCompleter(self.compSurBan2)

        self.ui.cBoxSurBan3.addItems(['']+strlstSur)
        self.compSurBan3 = QCompleter(strlstSur)
        self.compSurBan3.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurBan3.setCompleter(self.compSurBan3)

        self.ui.cBoxSurBan4.addItems(['']+strlstSur)
        self.compSurBan4 = QCompleter(strlstSur)
        self.compSurBan4.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurBan4.setCompleter(self.compSurBan4)

        self.ui.cBoxSurBan5.addItems(['']+strlstSur)
        self.compSurBan5 = QCompleter(strlstSur)
        self.compSurBan5.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurBan5.setCompleter(self.compSurBan5)

        self.ui.cBoxSurBan6.addItems(['']+strlstSur)
        self.compSurBan6 = QCompleter(strlstSur)
        self.compSurBan6.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurBan6.setCompleter(self.compSurBan6)

        self.ui.cBoxSurBan1.currentTextChanged.connect(self.updateSurBan1Pic)
        self.ui.cBoxSurBan2.currentTextChanged.connect(self.updateSurBan2Pic)
        self.ui.cBoxSurBan3.currentTextChanged.connect(self.updateSurBan3Pic)
        self.ui.cBoxSurBan4.currentTextChanged.connect(self.updateSurBan4Pic)
        self.ui.cBoxSurBan5.currentTextChanged.connect(self.updateSurBan5Pic)
        self.ui.cBoxSurBan6.currentTextChanged.connect(self.updateSurBan6Pic)

        # ban监管者
        self.ui.cBoxHunBan1.addItems(['']+strlstHun)
        self.compHunBan1 = QCompleter(strlstHun)
        self.compHunBan1.setFilterMode(Qt.MatchContains)
        self.ui.cBoxHunBan1.setCompleter(self.compHunBan1)

        self.ui.cBoxHunBan2.addItems(['']+strlstHun)
        self.compHunBan2 = QCompleter(strlstHun)
        self.compHunBan2.setFilterMode(Qt.MatchContains)
        self.ui.cBoxHunBan2.setCompleter(self.compHunBan2)

        self.ui.cBoxHunBan3.addItems(['']+strlstHun)
        self.compHunBan3 = QCompleter(strlstHun)
        self.compHunBan3.setFilterMode(Qt.MatchContains)
        self.ui.cBoxHunBan3.setCompleter(self.compHunBan3)

        self.ui.cBoxHunBan4.addItems(['']+strlstHun)
        self.compHunBan4 = QCompleter(strlstHun)
        self.compHunBan4.setFilterMode(Qt.MatchContains)
        self.ui.cBoxHunBan4.setCompleter(self.compHunBan4)

        self.ui.cBoxHunBan1.currentTextChanged.connect(self.updateHunBan1Pic)
        self.ui.cBoxHunBan2.currentTextChanged.connect(self.updateHunBan2Pic)
        self.ui.cBoxHunBan3.currentTextChanged.connect(self.updateHunBan3Pic)
        self.ui.cBoxHunBan4.currentTextChanged.connect(self.updateHunBan4Pic)

        # pick求生者
        self.ui.cBoxSurPick1.addItems(['']+strlstSur)
        self.compSurPick1 = QCompleter(strlstSur)
        self.compSurPick1.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurPick1.setCompleter(self.compSurPick1)

        self.ui.cBoxSurPick2.addItems(['']+strlstSur)
        self.compSurPick2 = QCompleter(strlstSur)
        self.compSurPick2.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurPick2.setCompleter(self.compSurPick2)

        self.ui.cBoxSurPick3.addItems(['']+strlstSur)
        self.compSurPick3 = QCompleter(strlstSur)
        self.compSurPick3.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurPick3.setCompleter(self.compSurPick3)

        self.ui.cBoxSurPick4.addItems(['']+strlstSur)
        self.compSurPick4 = QCompleter(strlstSur)
        self.compSurPick4.setFilterMode(Qt.MatchContains)
        self.ui.cBoxSurPick4.setCompleter(self.compSurPick4)

        self.ui.cBoxSurPick1.currentTextChanged.connect(self.updateSurPick1Pic)
        self.ui.cBoxSurPick2.currentTextChanged.connect(self.updateSurPick2Pic)
        self.ui.cBoxSurPick3.currentTextChanged.connect(self.updateSurPick3Pic)
        self.ui.cBoxSurPick4.currentTextChanged.connect(self.updateSurPick4Pic)

        # pick监管者
        self.ui.cBoxHunPick.addItems(['']+strlstHun)
        self.compHunPick = QCompleter(strlstHun)
        self.compHunPick.setFilterMode(Qt.MatchContains)
        self.ui.cBoxHunPick.setCompleter(self.compHunPick)

        self.ui.cBoxHunPick.currentTextChanged.connect(self.updateHunPickPic)

        # 生成bp界面
        self.ui.pBtnGen.clicked.connect(self.genFg)

    def swapTeam(self):
        temp = self.ui.lEdtSur.text()
        self.ui.lEdtSur.setText(self.ui.lEdtHun.text())
        self.ui.lEdtHun.setText(temp)

    def updateSurBan1Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurBan1.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurBan1Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan1Pic.setPixmap(pix)

    def updateSurBan2Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurBan2.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurBan2Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan2Pic.setPixmap(pix)

    def updateSurBan3Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurBan3.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurBan3Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan3Pic.setPixmap(pix)

    def updateSurBan4Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurBan4.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurBan4Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan4Pic.setPixmap(pix)

    def updateSurBan5Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurBan5.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurBan5Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan5Pic.setPixmap(pix)

    def updateSurBan6Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurBan6.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurBan6Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurBan6Pic.setPixmap(pix)

    def updateHunBan1Pic(self):
        pix = QPixmap()
        pix.load('./pic/hun/' + self.ui.cBoxHunBan1.currentText() + '.png')
        pix = pix.scaled(self.ui.labHunBan1Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan1Pic.setPixmap(pix)

    def updateHunBan2Pic(self):
        pix = QPixmap()
        pix.load('./pic/hun/' + self.ui.cBoxHunBan2.currentText() + '.png')
        pix = pix.scaled(self.ui.labHunBan2Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan2Pic.setPixmap(pix)

    def updateHunBan3Pic(self):
        pix = QPixmap()
        pix.load('./pic/hun/' + self.ui.cBoxHunBan3.currentText() + '.png')
        pix = pix.scaled(self.ui.labHunBan3Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan3Pic.setPixmap(pix)

    def updateHunBan4Pic(self):
        pix = QPixmap()
        pix.load('./pic/hun/' + self.ui.cBoxHunBan4.currentText() + '.png')
        pix = pix.scaled(self.ui.labHunBan4Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunBan4Pic.setPixmap(pix)

    def updateSurPick1Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurPick1.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurPick1Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick1Pic.setPixmap(pix)

    def updateSurPick2Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurPick2.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurPick2Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick2Pic.setPixmap(pix)

    def updateSurPick3Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurPick3.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurPick3Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick3Pic.setPixmap(pix)

    def updateSurPick4Pic(self):
        pix = QPixmap()
        pix.load('./pic/sur/' + self.ui.cBoxSurPick4.currentText() + '.png')
        pix = pix.scaled(self.ui.labSurPick4Pic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labSurPick4Pic.setPixmap(pix)

    def updateHunPickPic(self):
        pix = QPixmap()
        pix.load('./pic/hun/' + self.ui.cBoxHunPick.currentText() + '.png')
        pix = pix.scaled(self.ui.labHunPickPic.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.labHunPickPic.setPixmap(pix)

    def resetAll(self):
        self.ui.cBoxMap.setCurrentText('')
        self.ui.cBoxSurBan1.setCurrentText('')
        self.ui.cBoxSurBan2.setCurrentText('')
        self.ui.cBoxSurBan3.setCurrentText('')
        self.ui.cBoxSurBan4.setCurrentText('')
        self.ui.cBoxSurBan5.setCurrentText('')
        self.ui.cBoxSurBan6.setCurrentText('')
        self.ui.cBoxHunBan1.setCurrentText('')
        self.ui.cBoxHunBan2.setCurrentText('')
        self.ui.cBoxHunBan3.setCurrentText('')
        self.ui.cBoxHunBan4.setCurrentText('')
        self.ui.cBoxSurPick1.setCurrentText('')
        self.ui.cBoxSurPick2.setCurrentText('')
        self.ui.cBoxSurPick3.setCurrentText('')
        self.ui.cBoxSurPick4.setCurrentText('')
        self.ui.cBoxHunPick.setCurrentText('')

    def genFg(self):
        self.winFg = claWinFg()
        self.winFg.updateSurTeam(self.ui.lEdtSur.text())
        self.winFg.updateHunTeam(self.ui.lEdtHun.text())
        self.winFg.updateMap(self.ui.cBoxMap.currentText())
        self.winFg.updateSurBan1Pic(self.ui.cBoxSurBan1.currentText())
        self.winFg.updateSurBan2Pic(self.ui.cBoxSurBan2.currentText())
        self.winFg.updateSurBan3Pic(self.ui.cBoxSurBan3.currentText())
        self.winFg.updateSurBan4Pic(self.ui.cBoxSurBan4.currentText())
        self.winFg.updateSurBan5Pic(self.ui.cBoxSurBan5.currentText())
        self.winFg.updateSurBan6Pic(self.ui.cBoxSurBan6.currentText())
        self.winFg.updateHunBan1Pic(self.ui.cBoxHunBan1.currentText())
        self.winFg.updateHunBan2Pic(self.ui.cBoxHunBan2.currentText())
        self.winFg.updateHunBan3Pic(self.ui.cBoxHunBan3.currentText())
        self.winFg.updateHunBan4Pic(self.ui.cBoxHunBan4.currentText())
        self.winFg.updateSurPick1Pic(self.ui.cBoxSurPick1.currentText())
        self.winFg.updateSurPick2Pic(self.ui.cBoxSurPick2.currentText())
        self.winFg.updateSurPick3Pic(self.ui.cBoxSurPick3.currentText())
        self.winFg.updateSurPick4Pic(self.ui.cBoxSurPick4.currentText())
        self.winFg.updateHunPickPic(self.ui.cBoxHunPick.currentText())
        self.winFg.ui.show()

        # 修改队名
        self.ui.lEdtSur.textChanged.connect(self.winFg.updateSurTeam)
        self.ui.lEdtHun.textChanged.connect(self.winFg.updateHunTeam)

        # 选图
        self.ui.cBoxMap.currentTextChanged.connect(self.winFg.updateMap)

        # ban求生者
        self.ui.cBoxSurBan1.currentTextChanged.connect(self.winFg.updateSurBan1Pic)
        self.ui.cBoxSurBan2.currentTextChanged.connect(self.winFg.updateSurBan2Pic)
        self.ui.cBoxSurBan3.currentTextChanged.connect(self.winFg.updateSurBan3Pic)
        self.ui.cBoxSurBan4.currentTextChanged.connect(self.winFg.updateSurBan4Pic)
        self.ui.cBoxSurBan5.currentTextChanged.connect(self.winFg.updateSurBan5Pic)
        self.ui.cBoxSurBan6.currentTextChanged.connect(self.winFg.updateSurBan6Pic)

        # ban监管者
        self.ui.cBoxHunBan1.currentTextChanged.connect(self.winFg.updateHunBan1Pic)
        self.ui.cBoxHunBan2.currentTextChanged.connect(self.winFg.updateHunBan2Pic)
        self.ui.cBoxHunBan3.currentTextChanged.connect(self.winFg.updateHunBan3Pic)
        self.ui.cBoxHunBan4.currentTextChanged.connect(self.winFg.updateHunBan4Pic)

        # pick求生者
        self.ui.cBoxSurPick1.currentTextChanged.connect(self.winFg.updateSurPick1Pic)
        self.ui.cBoxSurPick2.currentTextChanged.connect(self.winFg.updateSurPick2Pic)
        self.ui.cBoxSurPick3.currentTextChanged.connect(self.winFg.updateSurPick3Pic)
        self.ui.cBoxSurPick4.currentTextChanged.connect(self.winFg.updateSurPick4Pic)

        # pick 监管者
        self.ui.cBoxHunPick.currentTextChanged.connect(self.winFg.updateHunPickPic)

if __name__ == '__main__':
    app = QApplication([])
    winBg = claWinBg()
    winBg.ui.show()
    app.exec()