<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Captura_de_Tela_com_Selenium_e_Envio_de_Email_0"></a>Captura de Tela com Selenium e Envio de Email</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Este script em Python utiliza o Selenium para capturar uma captura de tela de uma URL específica e, em seguida, envia um email com a captura de tela anexada. O script é projetado para ser executado a partir da linha de comando, aceitando argumentos de linha de comando para URL, caminho de saída para a captura de tela, assunto do email e corpo do email.</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Prrequisitos_4"></a>Pré-requisitos</h2>
<p class="has-line-data" data-line-start="6" data-line-end="7">Antes de executar o script, certifique-se de ter o seguinte:</p>
<ul>
<li class="has-line-data" data-line-start="8" data-line-end="9">
<p class="has-line-data" data-line-start="8" data-line-end="9"><strong>Python:</strong> <a href="https://www.python.org/downloads/">Instale o Python</a> em sua máquina.</p>
</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">
<p class="has-line-data" data-line-start="9" data-line-end="10"><strong>Navegador Chrome:</strong> <a href="https://www.google.com/chrome/">Instale o Chrome</a> em sua máquina.</p>
</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">
<p class="has-line-data" data-line-start="10" data-line-end="11"><strong>ChromeDriver:</strong> Adicione o executável ChromeDriver ao seu PATH do sistema ou defina a variável de ambiente <code>CHROMEDRIVER_PATH</code>.</p>
</li>
<li class="has-line-data" data-line-start="11" data-line-end="17">
<p class="has-line-data" data-line-start="11" data-line-end="12"><strong>Pacotes Python:</strong> Instale os pacotes necessários executando o seguinte comando no terminal:</p>
<pre><code class="has-line-data" data-line-start="14" data-line-end="16" class="language-bash">pip install selenium smtplib decouple
</code></pre>
</li>
</ul>
<h2 class="code-line" data-line-start=17 data-line-end=18 ><a id="Uso_17"></a>Uso</h2>
<ol>
<li class="has-line-data" data-line-start="19" data-line-end="25">
<p class="has-line-data" data-line-start="19" data-line-end="20">Clone o repositório em sua máquina local.</p>
<pre><code class="has-line-data" data-line-start="22" data-line-end="24" class="language-bash">git <span class="hljs-built_in">clone</span> https://github.com/your-username/selenium-screenshot-email.git
</code></pre>
</li>
<li class="has-line-data" data-line-start="25" data-line-end="31">
<p class="has-line-data" data-line-start="25" data-line-end="26">Navegue até o diretório do projeto.</p>
<pre><code class="has-line-data" data-line-start="28" data-line-end="30" class="language-bash"><span class="hljs-built_in">cd</span> selenium-screenshot-email
</code></pre>
</li>
<li class="has-line-data" data-line-start="31" data-line-end="44">
<p class="has-line-data" data-line-start="31" data-line-end="32">Crie um arquivo <code>.env</code> no diretório do projeto e adicione a seguinte configuração:</p>
<pre><code class="has-line-data" data-line-start="34" data-line-end="41" class="language-env">TO_EMAIL=seu_email@example.com
BCC_EMAIL=seu_bcc_email@example.com
SMTP_SERVER=seu_servidor_smtp.com
SMTP_PORT=587
SMTP_USER=seu_email@example.com
SMTP_PASSWORD=sua_senha_de_email
</code></pre>
<p class="has-line-data" data-line-start="42" data-line-end="43">Substitua os valores de espaço reservado pelos seus detalhes reais de email e servidor SMTP.</p>
</li>
<li class="has-line-data" data-line-start="44" data-line-end="56">
<p class="has-line-data" data-line-start="44" data-line-end="45">Execute o script com os argumentos de linha de comando necessários:</p>
<pre><code class="has-line-data" data-line-start="47" data-line-end="49" class="language-bash">python script.py &lt;URL&gt; &lt;Caminho_da_imagem&gt; &lt;Assunto&gt; &lt;Corpo&gt;
</code></pre>
<p class="has-line-data" data-line-start="50" data-line-end="51">Exemplo:</p>
<pre><code class="has-line-data" data-line-start="53" data-line-end="55" class="language-bash">python script.py https://example.com screenshots/screenshot.png <span class="hljs-string">"Instantâneo do Site"</span> <span class="hljs-string">"Confira o estado atual do site."</span>
</code></pre>
</li>
</ol>
<h2 class="code-line" data-line-start=56 data-line-end=57 ><a id="Argumentos_de_Linha_de_Comando_56"></a>Argumentos de Linha de Comando</h2>
<ul>
<li class="has-line-data" data-line-start="58" data-line-end="59"><code>URL</code>: A URL do site que você deseja capturar.</li>
<li class="has-line-data" data-line-start="59" data-line-end="60"><code>Caminho_da_imagem</code>: O caminho onde você deseja salvar a captura de tela.</li>
<li class="has-line-data" data-line-start="60" data-line-end="61"><code>Assunto</code>: O assunto do email.</li>
<li class="has-line-data" data-line-start="61" data-line-end="63"><code>Corpo</code>: O conteúdo do email.</li>
</ul>
<h2 class="code-line" data-line-start=63 data-line-end=64 ><a id="Notas_63"></a>Notas</h2>
<ul>
<li class="has-line-data" data-line-start="65" data-line-end="66">Certifique-se de configurar os detalhes do seu servidor de email no arquivo <code>.env</code>.</li>
<li class="has-line-data" data-line-start="66" data-line-end="67">O caminho do ChromeDriver é definido através da variável de ambiente <code>CHROMEDRIVER_PATH</code> ou tem o valor padrão <code>'C:\Program Files\Google\Chrome\chromedriver.exe'</code>.</li>
<li class="has-line-data" data-line-start="67" data-line-end="68">O script captura uma captura de tela usando um navegador Chrome sem interface gráfica.</li>
<li class="has-line-data" data-line-start="68" data-line-end="70">Em caso de erros, forneça os argumentos de linha de comando corretos conforme mostrado no exemplo.</li>
</ul>
<p class="has-line-data" data-line-start="70" data-line-end="71">Sinta-se à vontade para modificar e personalizar o script de acordo com suas necessidades. Se encontrar algum problema ou tiver sugestões de melhorias, por favor, abra um problema ou envie uma solicitação de pull.</p>
<hr>
<p class="has-line-data" data-line-start="74" data-line-end="75"><strong>Observação:</strong> Este documento foi formatado para visualização no GitHub. Se você deseja convertê-lo para HTML, pode usar ferramentas online como <a href="https://dillinger.io/">Dillinger</a> ou <a href="https://stackedit.io/">StackEdit</a>. Copie o conteúdo acima e cole em uma dessas ferramentas para gerar um HTML formatado.</p>