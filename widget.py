import sys
import re
import pandas as pd
from PyQt6.QtWidgets import (
    QFileDialog, QMessageBox, QAbstractItemView, QHeaderView, QTableWidgetItem, QMenu,
    QVBoxLayout, QHBoxLayout, QSizePolicy, QApplication, QWidget
)
from PyQt6.QtGui import QAction
from PyQt6 import QtCore

from form_ui import Ui_Widget  # Assuming you have this form UI class


class ItemSearchApp(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.show_context_menu)


        # Set up main layout
        main_layout = QVBoxLayout(self)

        # Layout for input fields and buttons
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.lineEdit)
        input_layout.addWidget(self.pushButton)
        input_layout.addWidget(self.lineEdit_2)
        input_layout.addWidget(self.pushButton_SelectFile)

        # Add the input layout to the main layout
        main_layout.addLayout(input_layout)

        # Make the table widget resize with the main window
        self.tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(self.tableWidget)

        # Set the layout for the main window
        self.setLayout(main_layout)


        # Table properties
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Sheet", "Summary", "Price"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)

        # Connect buttons
        self.pushButton_SelectFile.clicked.connect(self.select_file)
        self.pushButton.clicked.connect(self.search_item)
        self.lineEdit.returnPressed.connect(self.search_item)

        self.selected_file = None

    def show_context_menu(self, pos):
        item = self.tableWidget.itemAt(pos)
        if item is not None:
            if not item.isSelected():
                self.tableWidget.clearSelection()
                item.setSelected(True)

            context_menu = QMenu(self.tableWidget)
            copy_action = QAction("Copy", self)
            copy_action.triggered.connect(self.copy_to_clipboard)
            context_menu.addAction(copy_action)
            context_menu.exec(self.tableWidget.viewport().mapToGlobal(pos))

    def copy_to_clipboard(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            clipboard = QApplication.clipboard()
            text_to_copy = '\n'.join(item.text() for item in selected_items)
            clipboard.setText(text_to_copy)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.selected_file = file_path
            self.lineEdit_2.setText(file_path)

    def search_item(self):
        item_name = self.lineEdit.text().strip()
        self.tableWidget.setRowCount(0)

        if not self.selected_file:
            QMessageBox.warning(self, "No File Selected", "Please select an Excel file first.")
            return

        if not item_name:
            QMessageBox.warning(self, "No Item Name", "Please enter an item name to search.")
            return

        try:
            xls = pd.read_excel(self.selected_file, sheet_name=None)
            row_idx = 0

            for sheet_name, df in xls.items():
                results = df[df.apply(lambda row: row.astype(str).str.contains(item_name, case=False).any(), axis=1)]
                if not results.empty:
                    for _, row in results.iterrows():
                        values = row.astype(str).tolist()
                        number_like = [v for v in values if re.match(r'^[\d,.]+$', v)]
                        unit_price = None
                        if len(number_like) >= 2:
                            try:
                                unit_price = int(number_like[-2].replace(",", ""))
                            except ValueError:
                                pass
                        summary = " ".join(values[:6])
                        display_text = f"{unit_price if unit_price else 'N/A'}"

                        self.tableWidget.insertRow(row_idx)
                        self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(sheet_name))
                        self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(summary))
                        self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(display_text))
                        row_idx += 1

            if row_idx == 0:
                QMessageBox.information(self, "No Results", "No items found.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to read file:\n{str(e)}")




if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication for PyQt6
    window = ItemSearchApp()
    window.show()
    sys.exit(app.exec())







