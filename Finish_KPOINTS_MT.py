## 
#'''
#crawler for QE input file. Developed by Prof. Shin-Pon Ju at NSYSU
#
#1. anaconda for microsoft system:
#set 2 environmental parameters. For examples, add path for C:\Users\jushi\anaconda3\condabin and C:\Users\jushi\anaconda3
#
#2. chrome drive web for download:
#https://chromedriver.storage.googleapis.com/index.html
#watch out the following to check the proper version for chrome (type "chrome://settings/help" in your chrome brower first)
#selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 104
#Current browser version is 103.0.5060.134 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe
#selenium web source:
# https://www.byhy.net/tut/auto/selenium/01/
#'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
###---Explicit Waits-----
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
###---FilePath-----
import os
import pathlib
###---Regex---
import re
###----------------------------
os.remove('C:\\Users\\node\\selenium\\elementpath.txt') ### C:\\Users\\node\\selenium is current position  !!!
# os.remove('C:\\Users\\node\\selenium\\kpoints.dat')
# os.remove('C:\\Users\\node\\selenium\\kpointspath.dat') 
for dirPath, dirNames, fileNames in os.walk("C:\\Users\\node\\selenium\\single&binary"):  ### Modify to the directory folder where .cif is stored !!!
    # print(dirPath)
    for f in fileNames:
        if os.path.splitext(f)[1] == '.cif':
            elementspath = os.path.join(dirPath, f)
            # print(elementspath)
            with open('elementpath.txt', 'a') as elementspaths:
                elementspaths.write(''.join(elementspath)+"\r")
                elementspaths.close
###-----------Structurefile----------
with open('elementpath.txt', 'r') as infile:
    while True:
        line = infile.readline().splitlines()
        basename = os.path.basename(''.join(line))
        file_name = os.path.splitext(basename)[0]
        print(file_name)
        print(line)
        PATH = "C:/Users/node/selenium/chromedriver_win32/chromedriver.exe" ### Input chromedriver.exe Location & remember "/" not "\" !!!
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.materialscloud.org/work/tools/qeinputgenerator")### Input URL!!!
        ###----------Wait"Upload your structure"----------
        # WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.LINK_TEXT, "Upload your structure"))
        # )
        time.sleep(5)
        driver.switch_to.frame(0)  ###!!!
        Structurefile = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[1]/div[2]/input").send_keys(line) ### Input Structurefile Location
        # time.sleep(1)
        ###----------FileformatSelect----------
        fileformat = driver.find_element(By.ID, "fileformatSelect")
        fileformat.click()
        # time.sleep(1)
        # fileformat_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[2]/div[2]/select/option[1]")### Quantum ESPRESSO input [parser: qetools]
        # fileformat_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[2]/div[2]/select/option[2]")### CIF File (.cif) [parser: ase]
        fileformat_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[2]/div[2]/select/option[3]")### CIF File (.cif) [parser: pymatgen]
        fileformat_Select.click()
        # time.sleep(1)
        ###----------PseudoSelect----------
        Pseudo = driver.find_element(By.ID, "pseudoSelect")
        Pseudo.click()
        # time.sleep(1)
        # Pseudo_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[4]/div[2]/select/option[1]")### SSSP Efficiency PBEsol (version 1.1)
        # Pseudo_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[4]/div[2]/select/option[2]")### SSSP Precision PBEsol (version 1.1)
        Pseudo_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[4]/div[2]/select/option[3]")### SSSP Efficiency PBE (version 1.1)
        # Pseudo_Select = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[4]/div[2]/select/option[4]")### SSSP Precision PBE (version 1.1)
        Pseudo_Select.click()
        # time.sleep(1)
        ###----------MagnetizationSelect----------
        # Magnetization = driver.find_element(By.ID, "magnetizationSelect")
        # Magnetization.click()
        # time.sleep(1)
        # # MagnetizationSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[5]/div[2]/select/option[1]")### non-magnetic metal (fractional occupations)
        # # MagnetizationSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[5]/div[2]/select/option[2]")### non-magnetic insulator (fixed occupations)
        # MagnetizationSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[5]/div[2]/select/option[3]")### magnetic (fractional occupations)
        # MagnetizationSelect.click()
        # time.sleep(1)
        ###---------KmeshSelect-----------
        Kmesh = driver.find_element(By.ID, "kmeshSelect")
        Kmesh.click()
        # time.sleep(1)
        # KmeshSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[6]/div[2]/select/option[1]")### very fine (0.15 1/Å, 0.1 eV)
        # KmeshSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[6]/div[2]/select/option[2]")### fine (0.20 1/Å, 0.2 eV)
        KmeshSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[6]/div[2]/select/option[3]")### normal (0.30 1/Å, 0.3 eV)
        KmeshSelect.click()
        # time.sleep(1)
        ###----------RefineCellSelect----------
        # RefineCell = driver.find_element(By.ID, "refineCellSelect")
        # RefineCell.click()
        # time.sleep(1)
        # RefineCellSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[7]/div[2]/select/option[1]")### No
        # # RefineCellSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[7]/div[2]/select/option[2]")### Yes (choose the symmetry tolerance below)
        # RefineCellSelect.click()
        # time.sleep(1)
        ###----------Generate the PWscf input file----------
        Generate_the_PWscf_input_file = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[8]/input")
        Generate_the_PWscf_input_file.click()
        time.sleep(5)
        ###----------PWscf_input----------
        PWscf_inputs = driver.find_element(By.ID, "qepwinput")
        text = PWscf_inputs.text
        print(text)
        ###----------Cut KPOINTS---------- 
        Regex = r'\d+\s\d+\s\d+\s\d\s\d\s\d'
        KPOINTSRegex = re.compile(Regex)
        KPOINTS = KPOINTSRegex.findall(text)
        # print(type(KPOINTS))
        kpointpath=r'C:\Users\node\selenium\scf'        ### Modify to the directory folder where scf is stored !!!
        kpointspaths = os.path.join(kpointpath,file_name)
        print(kpointspaths)
        os.chdir(''.join(kpointspaths))         
        with open('kpoints.dat','w') as kpointsinfiles:
          kpointsinfiles.write(' '.join(KPOINTS))
          kpointsinfiles.close
          # os.getcwd()
          print(KPOINTS)
          time.sleep(1)
          print("Next!!!")
          driver.quit()
        if not line:
          break