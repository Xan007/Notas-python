from dataclasses import dataclass

@dataclass
class InventoryItem:
    nombre: str
    #Variable: tipo = valor defecto
    precio_unitario: float = 100
    cantidad: int = 1

    def total_cost(self) -> float:
        return self.precio_unitario * self.cantidad
    
Chocolate = InventoryItem("Chocolate")

print(Chocolate.total_cost())