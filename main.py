from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import parte1
import nueva3
import datetime
import credenciales  # Importa el módulo para solicitar credenciales

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

# Desplegar el menú desplegable
menu_desplegable_xpath = '//*[@id="dlDropDown"]'
menu_desplegable = wait.until(EC.element_to_be_clickable((By.XPATH, menu_desplegable_xpath)))
menu_desplegable.click()

# Esperar un momento para que el menú desplegable se abra completamente
driver.implicitly_wait(2)

# Hacer clic en el botón "Cargar" utilizando acciones del ratón
enlace_cargar_xpath = '//*[@id="opCargar"]'
enlace_cargar = wait.until(EC.element_to_be_clickable((By.XPATH, enlace_cargar_xpath)))
ActionChains(driver).move_to_element(enlace_cargar).click().perform()

# Hacer scroll hasta el elemento "fileDefinicion" para que sea visible
file_definicion_xpath = '//*[@id="fileDefinicion"]'
file_definicion = wait.until(EC.presence_of_element_located((By.XPATH, file_definicion_xpath)))
driver.execute_script("arguments[0].scrollIntoView(true);", file_definicion)

# Obtener la fecha actual
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")

# Construir la ruta del archivo CSV
archivo_ruta = fr'C:\reinicios\Reinicios_{fecha_actual}.csv'

# Ingresa la ruta del archivo en el campo correspondiente
file_definicion.send_keys(archivo_ruta)

# Hacer clic en el botón "Cargar masivo"
boton_cargar_masivo_xpath = '//*[@id="btnCargarMasivo"]'
boton_cargar_masivo = wait.until(EC.element_to_be_clickable((By.XPATH, boton_cargar_masivo_xpath)))
boton_cargar_masivo.click()
time.sleep(30)

# Hacer clic en el elemento deseado después de cargar el archivo
elemento_deseado_xpath = '//*[@id="infoMasivo"]/div/div/div[3]/button'
elemento_deseado = wait.until(EC.element_to_be_clickable((By.XPATH, elemento_deseado_xpath)))
elemento_deseado.click()
time.sleep(10)

# Esperar un breve momento para que la página cargue después de ingresar la ruta del archivo
driver.implicitly_wait(5)

# Ahora puedes continuar interactuando con la página según sea necesario
