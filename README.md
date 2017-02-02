# Netflix Generator #
Gerador de conta Netflix usando python2 e biblioteca Selenium v2.53.6

## Preparando para usar ##
### Instalar lib
    pip install selenium==2.53.6 
    
### Baixando repositório  
    sudo apt-get install git  
    git clone https://github.com/DavydMaker/netflix-generator.git  
    ou  
    wget https://github.com/DavydMaker/netflix-generator/archive/master.zip -O netflix-generator.zip  
    unzip netflix-generator.zip  
    cd netflix-generator
 
### Baixar ChromeDriver  
    Acesse https://sites.google.com/a/chromium.org/chromedriver/downloads para baixar o chromedriver.exe.    
    Depois é só especificar o local do arquivo se for utilizar o Google como navegador.
    
### Executando  
    python netflix-generator.py 
    
 Se quiser utilizar o Mozilla como navegador, altere a variável browser para Firefox.  
 O Mozilla já vem por padrão na instalação com o geckodriver, então não precisa especificar.
 
 Qualquer bug reportar para davydmaker@gmail.com por favor.
