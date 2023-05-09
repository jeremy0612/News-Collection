

#import os
import sys
from ui_interface import *
from  import_data import *
from PySide2.QtWidgets import QInputDialog ,QMessageBox

class MainWindow(QMainWindow):
    def __init__ (self, parent=None):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        text, ok = QInputDialog.getText(self, 'Server connection!', 'Enter password of your localhost:')
        if ok:
            print(text)
        try:
            connection = CONNECT("localhost", "root", text, "NewsCollection")
            article =  QUERY(connection, "select * from article;")
            author = QUERY(connection, "select * from author;")
            '''
            QUERY(connection,  """
                                    ALTER DATABASE NewsCollection
                                    CHARACTER SET utf8mb4
                                    COLLATE utf8mb4_unicode_ci;
                                    SET FOREIGN_KEY_CHECKS=0;
                                    LOAD DATA LOCAL INFILE 'C:/Users/nguye/Data.csv'
                                    INTO TABLE article
                                    FIELDS TERMINATED BY ','
                                    ENCLOSED BY '"'
                                    LINES TERMINATED BY '\n'
                                    IGNORE 1 ROWS;
                                """)
            
            '''
            self.ui.data = article
            self.ui.connection = connection
            self.ui.setupUi(self)

            self.show()
        except:
            QMessageBox.warning(self, 'Warning', 'Server connecting failed !')
            sys.exit()



        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())





























































 