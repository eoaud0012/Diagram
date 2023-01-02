import win32com.client
import pyautogui
import pyperclip
import openpyxl
import warnings
warnings.simplefilter("ignore")

wb = openpyxl.load_workbook("C:/Users/DW-PC/Desktop/이대명/DESK/공수/프로젝트 이력조회_20221212165205.xlsx")
wb.create_sheet('새시트이름',1)
ws = wb.active
ws.delete_rows(1)
ws.delete_rows(1)