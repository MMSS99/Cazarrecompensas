### De [How Reflex Works](https://reflex.dev/docs/advanced-onboarding/how-reflex-works/)
— !! All the state and logic are defined within a State class !!
— [Arquitectura de Reflex](https://reflex.dev/architecture.png)
— **VARS** se definen como atributos de clase State. Sólo se modifican por **EVENTOS**.
— **EVENT HANDLERS** son métodos en State. Se les llama como importación en el frontend: *on_blur=GithubState.set_profile*
— Por cada **EVENT HANDLER** activado, el State se actualiza. 

### De [Modelo-Vista-Controlador](https://github.com/dfleta/death-march/blob/main/code_complete/MVC.md)
— El **CONTROLADOR** del proyecto es Reflex y sus librerías que convierten Python a React y FastAPI. No programaremos sobre él, pero sí usamos sus **EVENT HANDLERS** 
— Las vistas serán lo que en los tutoriales es **INDEX**.
— El modelo son el **STATE** y módulos de Python que podemos importar a él. 