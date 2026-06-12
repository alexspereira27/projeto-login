import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode('dark')

# Criação das funções de funcinalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se usuario e senha
    if usuario == 'alex' and senha == '123456':
        resultado_login.configure(text='login feito com sucesso!',text_color='green')
    else:
        resultado_login.configure(text='Login incorreto!',text_color='red')

# Criação da janela principal
app = ctk.CTk()
app.title('Bytenordeste')
app.geometry('300x400')

# Criação dos campos
# Label
Label_usuario = ctk.CTkLabel(app,text='Usuário')
Label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
# Label
Label_senha = ctk.CTkLabel(app,text='Senha')
Label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha')
campo_senha.pack(pady=10)

# Button
botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)
# Campo feedback de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=40)


app.mainloop()