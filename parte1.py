from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import time
import credenciales  # Importa el módulo para solicitar credenciales

def ejecutar_todo():
    # Obtener las credenciales usando el módulo de credenciales
    usuario, contrasena = credenciales.obtener_credenciales_gui()

    # Opciones del navegador para ignorar los errores de certificado SSL
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')

    # Inicializa el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options)

    # Abre la página web
    driver.get("https://10.67.106.113/calidadgestion/index.php?SubMenu=Flujos%20NOW")

    # Espera a que aparezca el campo de usuario y luego ingresa el usuario
    wait = WebDriverWait(driver, 10)
    usuario_field = wait.until(EC.element_to_be_clickable((By.ID, "TFUsuario")))
    usuario_field.send_keys(usuario)

    # Espera a que aparezca el campo de contraseña y luego haz clic en él
    contrasena_field = wait.until(EC.element_to_be_clickable((By.ID, "TFContrasena")))
    contrasena_field.click()

    # Ingresa la contraseña
    contrasena_field.send_keys(contrasena)

    # Simula presionar la tecla Enter después de ingresar la contraseña
    contrasena_field.submit()

    # Espera un momento para que la página cargue completamente después del inicio de sesión
    driver.implicitly_wait(3)

    # Despliega el menú
    boton_menu_desplegable_xpath = '//*[@id="accordionSidebar"]/li[3]/a'
    boton_menu_desplegable = wait.until(EC.element_to_be_clickable((By.XPATH, boton_menu_desplegable_xpath)))
    boton_menu_desplegable.click()

    # Espera a que aparezca el enlace de los flujos
    enlace_flujos_xpath = '//*[@id="menu2"]/div/a[14]'
    enlace_flujos = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_flujos_xpath)))
    enlace_flujos.click()

    # Espera a que cargue la página después de hacer clic en el enlace
    driver.implicitly_wait(5)

    enlace_consulta_tab_xpath = '//*[@id="consulta-tab"]'
    enlace_consulta_tab = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_consulta_tab_xpath)))
    enlace_consulta_tab.click()

    enlace_consulta_tab_xpath = '//*[@id="dlDropDown"]'
    enlace_consulta_tab = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_consulta_tab_xpath)))
    enlace_consulta_tab.click()

    enlace_consulta_tab_xpath = '//*[@id="linkExport"]'
    enlace_consulta_tab = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_consulta_tab_xpath)))
    enlace_consulta_tab.click()

    enlace_fecha_desde_xpath = '//*[@id="fechaDesde"]'
    enlace_fecha_desde = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_fecha_desde_xpath)))
    enlace_fecha_desde.click()

    # Obtener la fecha del día anterior
    fecha_anterior = datetime.datetime.now() - datetime.timedelta(days=10)
    fecha_anterior_str = fecha_anterior.strftime("%Y-%m-%d")

    # Establecer el valor del campo de fecha utilizando JavaScript
    driver.execute_script(f"arguments[0].value = '{fecha_anterior_str}';", enlace_fecha_desde)
    enlace_fecha_desde.send_keys(Keys.ENTER)

    # Hacer clic en el campo de fecha "Fecha Hasta"
    enlace_fecha_hasta_xpath = '//*[@id="fechaHasta"]'
    enlace_fecha_hasta = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_fecha_hasta_xpath)))
    enlace_fecha_hasta.click()

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")

    # Establecer el valor del campo de fecha actual utilizando JavaScript
    driver.execute_script(f"arguments[0].value = '{fecha_actual}';", enlace_fecha_hasta)
    enlace_fecha_hasta.send_keys(Keys.ENTER)
    # Esperar un breve momento para asegurar que la fecha se haya establecido correctamente

    enlace_consulta_tab_xpath = '//*[@id="btnExportDef"]'
    enlace_consulta_tab = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_consulta_tab_xpath)))
    enlace_consulta_tab.click()

    enlace_consulta_tab_xpath = '//*[@id="modalExport"]/div/div/div[3]/button[2]'
    enlace_consulta_tab = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_consulta_tab_xpath)))
    enlace_consulta_tab.click()
    time.sleep(5)

    # Cerrar el navegador después de completar todos los procesos
    driver.quit()

# Llamar a la función para ejecutar todo el proceso
ejecutar_todo()
