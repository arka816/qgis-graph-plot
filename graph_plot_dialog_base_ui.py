# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\arka\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\graph_plot\graph_plot_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphPlotDialogBase(object):
    def setupUi(self, GraphPlotDialogBase):
        GraphPlotDialogBase.setObjectName("GraphPlotDialogBase")
        GraphPlotDialogBase.resize(742, 714)
        self.scrollArea = QtWidgets.QScrollArea(GraphPlotDialogBase)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 721, 691))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -500, 705, 1189))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 681, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.label.setObjectName("label")
        self.adj_file_path = QtWidgets.QLineEdit(self.groupBox)
        self.adj_file_path.setGeometry(QtCore.QRect(260, 40, 371, 31))
        self.adj_file_path.setObjectName("adj_file_path")
        self.adj_csv_loader = QtWidgets.QPushButton(self.groupBox)
        self.adj_csv_loader.setGeometry(QtCore.QRect(640, 40, 31, 31))
        self.adj_csv_loader.setObjectName("adj_csv_loader")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 261, 31))
        self.label_2.setObjectName("label_2")
        self.coords_file_path = QtWidgets.QLineEdit(self.groupBox)
        self.coords_file_path.setGeometry(QtCore.QRect(260, 90, 371, 31))
        self.coords_file_path.setObjectName("coords_file_path")
        self.coords_csv_loader = QtWidgets.QPushButton(self.groupBox)
        self.coords_csv_loader.setGeometry(QtCore.QRect(640, 90, 31, 31))
        self.coords_csv_loader.setObjectName("coords_csv_loader")
        self.load_vertices_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.load_vertices_btn.setGeometry(QtCore.QRect(470, 170, 221, 31))
        self.load_vertices_btn.setObjectName("load_vertices_btn")
        self.load_edges_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.load_edges_btn.setGeometry(QtCore.QRect(240, 170, 221, 31))
        self.load_edges_btn.setObjectName("load_edges_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 681, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.label_4.setObjectName("label_4")
        self.dot_file_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.dot_file_path.setGeometry(QtCore.QRect(260, 40, 371, 31))
        self.dot_file_path.setObjectName("dot_file_path")
        self.dot_file_loader = QtWidgets.QPushButton(self.groupBox_2)
        self.dot_file_loader.setGeometry(QtCore.QRect(640, 40, 31, 31))
        self.dot_file_loader.setObjectName("dot_file_loader")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 261, 31))
        self.label_5.setObjectName("label_5")
        self.save_file_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.save_file_path.setGeometry(QtCore.QRect(260, 90, 371, 31))
        self.save_file_path.setObjectName("save_file_path")
        self.dot_file_saver = QtWidgets.QPushButton(self.groupBox_2)
        self.dot_file_saver.setGeometry(QtCore.QRect(640, 90, 31, 31))
        self.dot_file_saver.setObjectName("dot_file_saver")
        self.load_graph_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.load_graph_btn.setGeometry(QtCore.QRect(240, 380, 221, 31))
        self.load_graph_btn.setObjectName("load_graph_btn")
        self.save_graph_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.save_graph_btn.setGeometry(QtCore.QRect(470, 380, 221, 31))
        self.save_graph_btn.setObjectName("save_graph_btn")
        self.log_box = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.log_box.setGeometry(QtCore.QRect(10, 430, 681, 181))
        self.log_box.setObjectName("log_box")
        self.adjacency_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.adjacency_table.setGeometry(QtCore.QRect(10, 630, 681, 301))
        self.adjacency_table.setObjectName("adjacency_table")
        self.adjacency_table.setColumnCount(0)
        self.adjacency_table.setRowCount(0)
        self.del_edge_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.del_edge_btn.setGeometry(QtCore.QRect(470, 940, 221, 31))
        self.del_edge_btn.setObjectName("del_edge_btn")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setGeometry(QtCore.QRect(10, 1020, 261, 31))
        self.label_3.setObjectName("label_3")
        self.edge_thres_slider = QtWidgets.QSlider(self.scrollAreaWidgetContents_2)
        self.edge_thres_slider.setGeometry(QtCore.QRect(290, 980, 351, 31))
        self.edge_thres_slider.setOrientation(QtCore.Qt.Horizontal)
        self.edge_thres_slider.setObjectName("edge_thres_slider")
        self.threshold_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.threshold_label.setGeometry(QtCore.QRect(670, 980, 21, 31))
        self.threshold_label.setObjectName("threshold_label")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(10, 980, 261, 31))
        self.label_6.setObjectName("label_6")
        self.top_edge_slider = QtWidgets.QSlider(self.scrollAreaWidgetContents_2)
        self.top_edge_slider.setGeometry(QtCore.QRect(290, 1020, 351, 31))
        self.top_edge_slider.setOrientation(QtCore.Qt.Horizontal)
        self.top_edge_slider.setObjectName("top_edge_slider")
        self.top_edge_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.top_edge_label.setGeometry(QtCore.QRect(670, 1020, 21, 31))
        self.top_edge_label.setObjectName("top_edge_label")
        self.plot_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.plot_btn.setGeometry(QtCore.QRect(10, 1110, 331, 31))
        self.plot_btn.setObjectName("plot_btn")
        self.commit_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.commit_btn.setGeometry(QtCore.QRect(360, 1110, 331, 31))
        self.commit_btn.setObjectName("commit_btn")
        self.close_layers_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.close_layers_btn.setGeometry(QtCore.QRect(10, 1150, 331, 31))
        self.close_layers_btn.setObjectName("close_layers_btn")
        self.screenshot_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.screenshot_btn.setGeometry(QtCore.QRect(360, 1150, 331, 31))
        self.screenshot_btn.setObjectName("screenshot_btn")
        self.calculate_edges = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.calculate_edges.setGeometry(QtCore.QRect(20, 1070, 331, 31))
        self.calculate_edges.setChecked(True)
        self.calculate_edges.setObjectName("calculate_edges")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(GraphPlotDialogBase)
        QtCore.QMetaObject.connectSlotsByName(GraphPlotDialogBase)
        GraphPlotDialogBase.setTabOrder(self.scrollArea, self.adj_file_path)
        GraphPlotDialogBase.setTabOrder(self.adj_file_path, self.adj_csv_loader)
        GraphPlotDialogBase.setTabOrder(self.adj_csv_loader, self.coords_file_path)
        GraphPlotDialogBase.setTabOrder(self.coords_file_path, self.coords_csv_loader)
        GraphPlotDialogBase.setTabOrder(self.coords_csv_loader, self.load_edges_btn)
        GraphPlotDialogBase.setTabOrder(self.load_edges_btn, self.load_vertices_btn)
        GraphPlotDialogBase.setTabOrder(self.load_vertices_btn, self.dot_file_path)
        GraphPlotDialogBase.setTabOrder(self.dot_file_path, self.dot_file_loader)
        GraphPlotDialogBase.setTabOrder(self.dot_file_loader, self.save_file_path)
        GraphPlotDialogBase.setTabOrder(self.save_file_path, self.dot_file_saver)
        GraphPlotDialogBase.setTabOrder(self.dot_file_saver, self.load_graph_btn)
        GraphPlotDialogBase.setTabOrder(self.load_graph_btn, self.save_graph_btn)
        GraphPlotDialogBase.setTabOrder(self.save_graph_btn, self.log_box)
        GraphPlotDialogBase.setTabOrder(self.log_box, self.adjacency_table)
        GraphPlotDialogBase.setTabOrder(self.adjacency_table, self.del_edge_btn)
        GraphPlotDialogBase.setTabOrder(self.del_edge_btn, self.edge_thres_slider)
        GraphPlotDialogBase.setTabOrder(self.edge_thres_slider, self.top_edge_slider)
        GraphPlotDialogBase.setTabOrder(self.top_edge_slider, self.calculate_edges)
        GraphPlotDialogBase.setTabOrder(self.calculate_edges, self.plot_btn)
        GraphPlotDialogBase.setTabOrder(self.plot_btn, self.commit_btn)
        GraphPlotDialogBase.setTabOrder(self.commit_btn, self.close_layers_btn)
        GraphPlotDialogBase.setTabOrder(self.close_layers_btn, self.screenshot_btn)

    def retranslateUi(self, GraphPlotDialogBase):
        _translate = QtCore.QCoreApplication.translate
        GraphPlotDialogBase.setWindowTitle(_translate("GraphPlotDialogBase", "GraphPlot"))
        self.groupBox.setTitle(_translate("GraphPlotDialogBase", "Load Raw Data"))
        self.label.setText(_translate("GraphPlotDialogBase", "Load adjacency matrix"))
        self.adj_csv_loader.setText(_translate("GraphPlotDialogBase", "..."))
        self.label_2.setText(_translate("GraphPlotDialogBase", "Load Vertex coordinates"))
        self.coords_csv_loader.setText(_translate("GraphPlotDialogBase", "..."))
        self.load_vertices_btn.setText(_translate("GraphPlotDialogBase", "LOAD VERTICES"))
        self.load_edges_btn.setText(_translate("GraphPlotDialogBase", "LOAD EDGES"))
        self.groupBox_2.setTitle(_translate("GraphPlotDialogBase", "Dot file I/O"))
        self.label_4.setText(_translate("GraphPlotDialogBase", "Load Dot File"))
        self.dot_file_loader.setText(_translate("GraphPlotDialogBase", "..."))
        self.label_5.setText(_translate("GraphPlotDialogBase", "Save Dot File"))
        self.dot_file_saver.setText(_translate("GraphPlotDialogBase", "..."))
        self.load_graph_btn.setText(_translate("GraphPlotDialogBase", "LOAD GRAPH"))
        self.save_graph_btn.setText(_translate("GraphPlotDialogBase", "SAVE GRAPH"))
        self.del_edge_btn.setText(_translate("GraphPlotDialogBase", "DELETE EDGE"))
        self.label_3.setText(_translate("GraphPlotDialogBase", "Choose Edge weight threshold"))
        self.threshold_label.setText(_translate("GraphPlotDialogBase", "-"))
        self.label_6.setText(_translate("GraphPlotDialogBase", "Choose heaviest N edges"))
        self.top_edge_label.setText(_translate("GraphPlotDialogBase", "-"))
        self.plot_btn.setText(_translate("GraphPlotDialogBase", "PLOT GRAPH"))
        self.commit_btn.setText(_translate("GraphPlotDialogBase", "COMMIT CHANGES"))
        self.close_layers_btn.setText(_translate("GraphPlotDialogBase", "CLOSE LAYERS"))
        self.screenshot_btn.setText(_translate("GraphPlotDialogBase", "SCREENSHOT CANVAS"))
        self.calculate_edges.setText(_translate("GraphPlotDialogBase", "Calculate edges?"))
