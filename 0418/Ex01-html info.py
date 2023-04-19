'''
URL(Uniform Resource Locator)
    인터넷에서 웹 페이지, 이미지, 동영상 등과 같은 리소스를 찾을 수 있는 주소

https://news.nate.com/rank/?mid=n1000
프로토콜(protocol)
    컴퓨터 네트워크를 통해 통신을 수행하기 위한 표준화된 규칙, 절차, 혹은 통신 프로세스를 의미
    통신하는 당사자간에 서로 어떤 식으로 데이터를 주고받을 지 정해놓은 규칙
    ex) 
        http/https : Hyper Text Trasfer Protocol 웹서버 접속
        http : 데이터를 보낼 때 데이터를 그대로 보냄 
        https : 데이터를 보내기 전에 암호화를 하고, 데이터를 받는 서버에 인증요구를 한다.
        ftp : 파일 서버 접속할 때 사용
        mailto : 메일 서버 접속할 때 사용
        telnet : 원격지 접속
        
호스트(host)
    아파트 주소로 따지면 동 까지
    리소스가 위치한 서버의 이름
    ex) news.nate.com
    사실은 IP로 접속하는 것이다.
    
포트(port)
    서버에서 사용하는 방 번호
    호스트 뒤에 ':443'
    디폴트 값은 표시하지 않고 생략한다.
    ex)
        http : 80
        https : 443
        https://news.nate.com/rank/?mid=n1000 == https://news.nate.com:443/rank/?mid=n1000
    
포트까지가 실제 주소이다.

경로(path)
    웹서버에서 리소스에 대한 경로(물리적 또는 추상적 경로)
    ex) /rank
    
쿼리(query)
    추가로 서버에 보내는 파라미터. 물음표 뒤에 온다.
    ex) ?mid=n1000
        ?key1=value1&key2=value2&key3=value3
    get() : 파라미터를 노출한다. 위의 mid=n1000과 같음.
    post() : 파라미터를 노출시키지 않는다.
    
    
'''