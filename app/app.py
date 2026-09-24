from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
	return """
	<!DOCTYPE html>
	<html lang="pt-BR">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Meu Site</title>
		<style>
			/* Estilos gerais (Decoração da página) */
			body {
				font-family: Arial, sans-serif;
				background-color: #f4f4f9;
				margin: 0;
            			display: flex;
				flex-direction: column;
            			justify-content: center;
            			align-items: center;
            			height: 100vh;
        		}
			
			.titulo-principal {
				color: #333;
				margin-bottom: 5px;
				text-align: center;
			}
			
			.subtitulo-principal {
				color: #666;
				margin-bottom: 30px;
				text-align: center;
			}

			.container {
            			text-align: center;
            			background: white;
            			padding: 40px;
            			border-radius: 12px;
            			box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
				max-width: 400px;
        		}

			h2 {
            			color: #333;
            			margin-bottom: 20px;
        		}

        		/* Estilo dos Botões */
        		.btn {
            			display: inline-block;
            			padding: 12px 24px;
            			margin: 5px;
            			font-size: 16px;
            			font-weight: bold;
            			text-decoration: none; /* Remove o sublinhado padrão do link */
            			color: white;
            			background-color: #007bff; /* Cor azul do botão */
            			border-radius: 8px; /* Arredonda as bordas */
            			transition: background-color 0.3s ease; /* Efeito suave ao passar o mouse */
        		}

        /* Cor diferente para o botão de contato (opcional) */
        		.btn-contato {
            			background-color: #28a745; /* Cor verde */
        		}

        /* Efeito quando o mouse passa por cima do botão */
        		.btn:hover {
            			background-color: #0056b3;
        		}

        		.btn-contato:hover {
            			background-color: #1e7e34;
        		}
		</style>
	</head>
	<body>

		<h1>Bem-vindo ao meu site</h1>
		<p>Escolha uma das opções abaixo para saber mais:</p>
        
        	<!-- Quadro -->
		<div class="container">
			<h2>Bem-vindo ao nosso site</h2>
			<p>Escolha uma das opções abaixo para saber mais:</p>
        
        		<a href="/sobre" class="btn">Sobre</a>
        		<a href="/contato" class="btn btn-contato">Contato</a>
    		</div>

	</body>
	</html>
	"""

@app.route("/contato")
def contato():
    	return"""
	<p>contato 1: jennyfer.mello@aluno.ifsp.edu.br</p>
	<p>contato 2: s.jenifer@aluno.ifsp.edu.br</p>
	<br>
	<a href="/">Voltar para o Início</a>
	"""

@app.route("/sobre")
def sobre():
	return"""
	<h1>Sobre</h1>
      	<p>Usando o docker</p>
	<br>
	<a href="/">Voltar para o Início</a>
   	"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

