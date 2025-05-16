import prova_escrita_03 
import prova_escrita_04 
import unittest 

class test_prova_escrita_03(unittest.TestCase): # Creem la classe test_prova_escrita_03
    """
    Tests de la prova_escrita_03
    """
    
    def test_trobar_max_min_rendiment(self): # Funció test_trobar_max_min_rendiment
        """
        Funció pel test funció trobar_max_min_rendiment
        """
        
        resultat = prova_escrita_03.trobar_min_max_rendiment(10.50, 12.00, 15.00) # Crida de la funció amb 3 paràmetres
        self.assertEqual(resultat, (10.50, 15.00)) # Verifiquem resultat
        
        resultat1 = prova_escrita_03.trobar_min_max_rendiment() # Crida de la funció sense paràmetres
        self.assertEqual(resultat1, (0, 0)) # Verifiquem resultat 
        
        resultat2 = prova_escrita_03.trobar_min_max_rendiment(10.50, 10.50, 10.50) # Crida de la funció amb els paràmetres iguals 
        self.assertEqual(resultat2, (10.50, 10.50)) # Verifiquem resultat 

    def test_comptar_estudiants(self): # Funció test_comptar_estudiants
        """
        Tests de comptar_estudiants
        """

        resultat = prova_escrita_03.comptar_estudiants(prova_escrita_03.notes_estudiants) # Crida de la funció amb el dic notes_estudiants
        self.assertEqual(resultat, (4)) # Verifiquem resultat  

    def test_comptar_estudiants_matèria(self): # Funció test_comptar_estudiants_matèria
        """
        Tests de comptar_estudiants_matèria
        """

        resultat = prova_escrita_03.comptar_estudiants_matèria(prova_escrita_03.notes_estudiants, "Història") # Crida de la funció amb el dic notes_estudiants i matèria "Història"
        self.assertEqual(resultat, (2)) # Verifiquem resultat  
    
class test_prova_escrita_04(unittest.TestCase): # Classe test_prova_escrita_04
    """
    Tests prova_escrita_04
    """
    
    def test_cercar_el(self): # Creem la funció test_cercar_el
        """
        Tests de funció cercar_el
        """
        
        resultat = prova_escrita_04.cercar_el(prova_escrita_04.m_ex, 4, mostrar_posicio=False) # Crida de la funció amb la matriu m_ex, el valor 4 i mostrar_posicio=False
        self.assertEqual(resultat, (True, None)) # Comprovem resultat  
        
        resultat1 = prova_escrita_04.cercar_el(prova_escrita_04.m_ex, 2, mostrar_posicio=True) # Crida de la funció amb la matriu m_ex, el valor 2 i mostrar_posicio=True
        self.assertEqual(resultat1, (True, (0, 1))) # Comprovem resultat  
        
        resultat2 = prova_escrita_04.cercar_el(prova_escrita_04.m_ex, 99, mostrar_posicio=True) # Crida de la funció amb la matriu m_ex, el valor 99 i mostrar_posicio=True
        self.assertEqual(resultat2, (False, None)) # Comprovem resultat  
        
    def test_sumar_fila(self): # Funció test de la funció sumar_fila
        """
        Test de la funció sumar_fila
        """
        
        resultat = prova_escrita_04.sumar_fila(prova_escrita_04.m_ex, index=0) # Crida de la funció amb la matriu m_ex i index=0
        self.assertEqual(resultat, (6)) # Comprovem resultat  
        
        resultat1 = prova_escrita_04.sumar_fila(prova_escrita_04.m_ex, index=99) # Crida de la funció amb la matriu m_ex i index=99
        self.assertEqual(resultat1, None) # Comprovem resultat  

    def test_sumar_matriu(self):
        """
        Test de la funció sumar_matriu
        """
        
        resultat = prova_escrita_04.sumar_matriu(prova_escrita_04.m_ex) # Crida de la funció amb la matriu m_ex
        self.assertEqual(resultat, 45) # Comprovem resultat

    def test_transformar(self):
        """
        Test de la funció transformar
        """

        l = prova_escrita_04.m_ex[:] # Còpia de la matriu m_ex
        
        prova_escrita_04.transformar(l, 10, "*") # Crida de la funció amb l, 10 i "*"
        self.assertEqual(l, [[10, 20, 30], [40, 50, 60], [70, 80, 90]]) # Comprovem resultat
        
if __name__ == '__main__':
    unittest.main()