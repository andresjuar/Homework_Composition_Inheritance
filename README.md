# Homework_Composition_Inheritance

Este proyecto contiene dos implementaciones de un sistema de manejo de empleados en Python:

* **Composition:** implementación utilizando composición.
* **Inheritance:** implementación utilizando herencia.

Ambas implementaciones buscan resolver el mismo problema y producen una salida equivalente. La diferencia principal está en la forma en que se relacionan y organizan las clases.

## Estructura del proyecto

```text
Homework_Composition_Inheritance/
│
├── composition/
│ ├── Commission.py 
│ ├── Contract.py 
│ ├── ContractComission.py 
│ ├── Employee.py 
│ ├── FreelancerContract.py 
│ ├── HourlyContract.py 
│ ├── main.py 
│ └── SalariedContract.py
│
├── inheritance/
|   ├── Employee.py 
|   ├── Freelancer.py 
|   ├── HourlyEmployee.py 
|   ├── main.py 
|   ├── SalariedEmployee.py 
│   └── withCommission/ 
|       ├── FreelancerWithCommission 
|       ├── HourlyEmployeeWithCommission.py 
|       └── SalariedEmployeeWithCommission.py
│
└── README.md
```

Cada carpeta contiene su propia implementación y un archivo `main.py` utilizado para probar el funcionamiento del sistema. Este archivo está basado en el main del video

## Ejecución

Para ejecutar cualquiera de las implementaciones, entra a la carpeta correspondiente y ejecuta su archivo `main.py`.

### Composition

```bash
cd composition
python main.py
```

### Inheritance

```bash
cd inheritance
python main.py
```
