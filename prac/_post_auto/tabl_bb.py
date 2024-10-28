# TABL
import xlsxwriter
from bb import get_disc_autor

def writer(parametr):
      book = xlsxwriter.Workbook(r'D:\Works\Python\____3_kurs_works\pred_cen_kvar\prac\_post_auto\bb_tabl.xlsx')
      page = book.add_worksheet("Товар")

      row = 0
      column = 0

      page.set_column("A:A", 60)
      page.set_row(0, 100)
      page.set_column("B:B", 40)

      for item in parametr():
            page.write(row, column, item[0])
            page.write(row, column+1, item[1])
            row+=1
      
      book.close()

writer(get_disc_autor)