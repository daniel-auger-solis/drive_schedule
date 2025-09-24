## 🚀 Ejecución programada del workflow

GitHub Actions permite usar `schedule` con sintaxis de cron para ejecutar automáticamente workflows.  
Sin embargo, **no es 100% confiable**: las ejecuciones pueden retrasarse 40 minutos, 1 hora o incluso más debido a las colas internas de GitHub.  

Para un **schedule mucho más preciso y fiable**, es recomendable usar [cron-job.org](https://cron-job.org), un servicio gratuito que dispara una petición HTTP en el intervalo exacto que definas.  

---

### 🔧 Configuración en cron-job.org

1. **Crear un nuevo cron job**  
   - En la pestaña **Common**:
     - **Title**: escribe un nombre para tu job (ej: `Run drive_schedule`).
     - **URL**: usa el endpoint de GitHub para ejecutar tu workflow:  
       ```
       https://api.github.com/repos/daniel-auger-solis/drive_schedule/actions/workflows/actions.yml/dispatches
       ```
     - **Execution Schedule**: define cada cuánto tiempo quieres que se ejecute (ej: cada 30 minutos).  
   - En la pestaña **Advanced** puedes dejar las opciones por defecto.

2. **Configurar los Headers**  
   Agrega los siguientes encabezados (Key → Value):  
   - `Authorization` → `token TU_GITHUB_PERSONAL_ACCESS_TOKEN`  
   - `Accept` → `application/vnd.github+json`  
   - `Content-Type` → `application/json`

3. **Obtener tu token de GitHub**  
   - Ve a [Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens).  
   - Genera un token con permisos:
     - `workflow`
     - `repo` (si tu repo es privado)  
   - Copia el token generado y úsalo en el header `Authorization`.

4. **Configurar el método y el body**  
   - **Request Method**: `POST`  
   - **Request Body**:  
     ```json
     {
       "ref": "master"
     }
     ```
     > Aquí `"master"` corresponde a la rama principal del repositorio.

---

### ✅ Verificación

Para confirmar que todo funciona:  
1. Ve a tu repositorio en GitHub.  
2. Entra a la pestaña **Actions**.  
3. Verás una nueva ejecución de tu workflow justo en el horario definido en cron-job.org.  

Si aparece ahí, ¡todo está funcionando correctamente! 🎉
