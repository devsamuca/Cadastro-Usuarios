import mysql.connector
from customtkinter import *
from tkinter import messagebox

#Conexão com o Banco
def Conexao():
    try:
        conexao = mysql.connector.connect(
            host="###",
            user="###",
            password="###",
            database="###"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao realizar Conexão! {erro}")
        return None
#Armazenando o Resultado da Função Conexão
db = Conexao()

#Função para Cadastrar Usuário
def Cadastro_User():
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT INTO users (nome, data, sexo) VALUES (%s, %s,  %s)"
        if option_sexo.get() == "Masculino":
            valores = (digitNome.get(), digitData.get(), "M")
        if option_sexo.get() == "Feminino":
            valores = (digitNome.get(), digitData.get(), "F")
        
        #Validação dos Dados
        if not digitNome.get():
            messagebox.showerror("Erro", "O Nome não pode estar vazio!")
            return
        if len(digitData.get()) != 10 or digitData.get()[4] != '-' or digitData.get()[7] != '-':
            messagebox.showerror("Erro", "A Data de nascimento deve estar no formato YYYY-MM-DD!")
            return
        
        try:
            cursor.execute(sql, valores)
            db.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro", f"Falha ao cadastrar: {erro}")
        finally:
            cursor.close()
            db.close()
    else:
        messagebox.showerror("Erro", "Conexão ao banco falhou!")

#Iniciando App
App = CTk()

#Config do App
App._set_appearance_mode("light")
App.title("Cadastro")
App.geometry("300x360")
App.resizable(False, False)
App.iconbitmap("icon.ico")

#Centralizar
def CentralizaWindow():
    App.update()
    screenX = App.winfo_screenwidth()
    screenY = App.winfo_screenheight()
    WindowX = App.winfo_width()
    WindowY = App.winfo_height()
    PosX = (screenX//2) - (WindowX//2)
    PosY = (screenY//2) - (WindowY//2)
    App.geometry(f"{WindowX}x{WindowY}+{PosX}+{PosY}")
CentralizaWindow()

#Titulo
Title = CTkLabel(App, text="Cadastrar Usuário", text_color="black", font=("Arial", 20), bg_color="#EBEBEB")
Title.pack(pady=10)

#Nome
Name = CTkLabel(App, text="Nome:", text_color="black", font=("Arial", 15), bg_color="#EBEBEB", justify="right")
Name.pack(padx=(0, 5), pady=(10, 0))

digitNome = CTkEntry(App, width=200, bg_color="#EBEBEB",fg_color="#ffffff", placeholder_text="Digite Aqui",text_color="black",corner_radius=100)
digitNome.pack(pady=5)


#Data de Nascimento
DataNasc = CTkLabel(App, text="Data de Nascimento:", text_color="black", font=("Arial", 15), bg_color="#EBEBEB", justify="right")
DataNasc.pack(padx=(0, 5), pady=(10, 0))

digitData = CTkEntry(App, width=200,placeholder_text="YYYY-MM-DD",bg_color="#EBEBEB", fg_color="#ffffff",text_color="black",corner_radius=100)
digitData.pack(pady=5)

#Sexo
Sexo = CTkLabel(App, text="Sexo:", text_color="black", font=("Arial", 15), bg_color="#EBEBEB", justify="right")
Sexo.pack(padx=(0, 5), pady=(10, 0))

option_sexo = CTkOptionMenu(App, values=["Masculino", "Feminino"],bg_color="#EBEBEB")
option_sexo.pack(pady=5)

#Botão
btn_cadastrar = CTkButton(App, text="Cadastrar",font=("Arial",17), command=Cadastro_User,height=40,width=100,bg_color="#EBEBEB")
btn_cadastrar.pack(pady=20)

App.mainloop()
