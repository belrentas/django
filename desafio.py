class Funcionarios:
    
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        
    def AgendarConsulta(self, nome_paciente, data):
        self.nome_paciente = nome_paciente
        self.data = data
        
        print(f'''Consulta agendada com sucesso:
              
              Paciente: {self.nome_paciente}
              Data: {self.data}
              
              ''')
    
    def RealizarExame(self):
        
        print(f'Exame realizado por {self.nome}.')


class Enfermeiro(Funcionarios):
    
    def __init__(self, nome, especialidade, coren):
        Funcionarios.__init__(self,nome,especialidade)
        self.coren = coren    
    
    def AplicarInjecao(self, tipo):
        self.tipo = tipo
        print(f'Aplicação de {self.tipo} será efetuada...')    
        

class Medico(Funcionarios):
    
    def __init__(self, nome, especialidade, CRM):
        Funcionarios.__init__(nome, especialidade)
        self.crm = CRM
        
    def Preescricao(self, Diagnostico, Receita):
        self.diagnostico = Diagnostico
        self.receita = Receita
        
        print(f'''
              -----PRESCRIÇÃO------
              
              Diagnóstico: {self.diagnostico}
              Receita: {self.receita}
              
              ''')
        
if __name__ == '__main__':
    Medico = Medico('Camila', 'Dermato', 2707)
    Enfermeiro = Enfermeiro('Eminem', 'Chefe', 205)
    
    #Medico
    Medico.AgendarConsulta('Isabel', '08/05/2024')
    Medico.RealizarExame()
    Medico.Preescricao('Covid-19', 'Dipirona')
    
    #Enfermeiro
    Enfermeiro.AgendarConsulta('Bruno', '07/08/2024')
    Enfermeiro.RealizarExame()
    Enfermeiro.AplicarInjecao('Dipirona')
    
    