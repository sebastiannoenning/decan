self.page_addevent = QWidget()
        self.page_addevent.setObjectName(u"page_addevent")
        self.eventform = QScrollArea(self.page_addevent)
        self.eventform.setObjectName(u"eventform")
        self.eventform.setGeometry(QRect(310, 0, 341, 461))
        self.eventform.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 339, 459))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 331, 385))
        self.generalcontainer = QVBoxLayout(self.verticalLayoutWidget)
        self.generalcontainer.setObjectName(u"generalcontainer")
        self.generalcontainer.setContentsMargins(0, 0, 0, 0)
        self.GenericSettings = QFormLayout()
        self.GenericSettings.setObjectName(u"GenericSettings")
        self.label_user = QLabel(self.verticalLayoutWidget)
        self.label_user.setObjectName(u"label_user")

        self.GenericSettings.setWidget(0, QFormLayout.LabelRole, self.label_user)

        self.selectuser = QComboBox(self.verticalLayoutWidget)
        self.selectuser.setObjectName(u"selectuser")

        self.GenericSettings.setWidget(0, QFormLayout.FieldRole, self.selectuser)

        self.label_title = QLabel(self.verticalLayoutWidget)
        self.label_title.setObjectName(u"label_title")

        self.GenericSettings.setWidget(1, QFormLayout.LabelRole, self.label_title)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.GenericSettings.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_st = QLabel(self.verticalLayoutWidget)
        self.label_st.setObjectName(u"label_st")

        self.GenericSettings.setWidget(2, QFormLayout.LabelRole, self.label_st)

        self.startedit = QDateTimeEdit(self.verticalLayoutWidget)
        self.startedit.setObjectName(u"startedit")

        self.GenericSettings.setWidget(2, QFormLayout.FieldRole, self.startedit)

        self.label_et = QLabel(self.verticalLayoutWidget)
        self.label_et.setObjectName(u"label_et")

        self.GenericSettings.setWidget(3, QFormLayout.LabelRole, self.label_et)

        self.endedit = QDateTimeEdit(self.verticalLayoutWidget)
        self.endedit.setObjectName(u"endedit")

        self.GenericSettings.setWidget(3, QFormLayout.FieldRole, self.endedit)


        self.generalcontainer.addLayout(self.GenericSettings)

        self.expandusers = QPushButton(self.verticalLayoutWidget)
        self.expandusers.setObjectName(u"expandusers")

        self.generalcontainer.addWidget(self.expandusers)

        self.userview = QListView(self.verticalLayoutWidget)
        self.userview.setObjectName(u"userview")

        self.generalcontainer.addWidget(self.userview)

        self.componentsexpand = QVBoxLayout()
        self.componentsexpand.setObjectName(u"componentsexpand")
        self.expandcomponent = QPushButton(self.verticalLayoutWidget)
        self.expandcomponent.setObjectName(u"expandcomponent")

        self.componentsexpand.addWidget(self.expandcomponent)

        self.select_add = QHBoxLayout()
        self.select_add.setObjectName(u"select_add")
        self.selectcomponenttype = QComboBox(self.verticalLayoutWidget)
        self.selectcomponenttype.setObjectName(u"selectcomponenttype")

        self.select_add.addWidget(self.selectcomponenttype)

        self.addcomponent = QPushButton(self.verticalLayoutWidget)
        self.addcomponent.setObjectName(u"addcomponent")

        self.select_add.addWidget(self.addcomponent)


        self.componentsexpand.addLayout(self.select_add)

        self.dynamiccomponentsection = QVBoxLayout()
        self.dynamiccomponentsection.setObjectName(u"dynamiccomponentsection")

        self.componentsexpand.addLayout(self.dynamiccomponentsection)


        self.generalcontainer.addLayout(self.componentsexpand)

        self.addeventbutton = QPushButton(self.verticalLayoutWidget)
        self.addeventbutton.setObjectName(u"addeventbutton")

        self.generalcontainer.addWidget(self.addeventbutton)