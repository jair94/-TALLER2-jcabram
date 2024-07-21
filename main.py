from models.huron import Huron
from models.boa_Constrictor import Boa_Constrictor
from models.guarderia import Guarderia


class Main:
    @staticmethod
    def main():
        guarderia = Guarderia()
        
        huron = guarderia.huron1
        huron2 = guarderia.huron2
        boa = guarderia.boa1
        boa2 = guarderia.boa2

        # Probando Huron
        print("-----------")
        # Información del Animal exótico
        print("Información Animal Exótico:")
        print(huron)
        # Sonido Huron
        print(f"{huron.obtener_nombre()} suena: {huron.hacer_sonido()}") 
        # Probando cálculo de flete
        print(f"Flete Hurón: {huron.calcular_flete()}") 
        print("-----------")

        # Información del Animal exótico
        print("Información Animal Exótico:")
        print(huron2)
        # Sonido Huron
        print(f"{huron2.obtener_nombre()} suena: {huron2.hacer_sonido()}")  
        # Probando cálculo de flete
        print(f"Flete Hurón: {huron2.calcular_flete()}") 
        print("-----------")

        # Información del Animal exótico
        print("Información Animal Exótico:")
        print(boa)
        # Sonido Huron
        print(f"{boa.obtener_nombre()} suena: {boa.hacer_sonido()}")  
        # Probando cálculo de flete
        print(f"Flete Boa: {boa.calcular_flete()}") 
         # Probando método comer_ratones
        print(f"Dar ratones a la Boa...")  
        boa.comer_ratones()
        boa.comer_ratones()
        print(f"Ratones comidos: {boa.ratones_comidos}")  # Verificar que ratones_comidos incrementó
        print("-----------")

        # Información del Animal exótico
        print("Información Animal Exótico:")
        print(boa2)
        # Sonido Huron
        print(f"{boa2.obtener_nombre()} suena: {boa2.hacer_sonido()}")  
        # Probando cálculo de flete
        print(f"Flete Boa: {boa2.calcular_flete()}") 
         # Probando método comer_ratones
        print(f"Dar ratones a la Boa...")
        try:
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones()
            boa2.comer_ratones() 
            boa2.comer_ratones() # Esto debería lanzar el ValueError
        except ValueError as e:
            print(e)
        print(f"Ratones comidos: {boa2.ratones_comidos}")  # Verificar que ratones_comidos incrementó
        print("-----------") 
        print(f"Alimentar boa: {guarderia.alimentar_boa(boa2)}")

        


if __name__ == "__main__":
    Main.main()
