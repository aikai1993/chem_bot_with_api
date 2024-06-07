from fastapi import FastAPI
from .utils import result_calc

app = FastAPI()


@app.get('/calc/{brt}')
async def calc(brt: str) -> dict:
    return result_calc(brt)

@app.get('/calc_exact/{brt}')
async def calc_exact(brt: str) -> dict:
    return result_calc(brt, exact=True)

@app.get('/mol_mass/{brt}')
async def mol_mass(brt : str) -> float:
    return result_calc(brt)['total_mass']

@app.get('/elem_analysis/{brt}')
async def elem_analysis(brt : str) -> dict:
    return result_calc(brt)['elements']