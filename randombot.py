import discord
import asyncio
import random 
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
    if message.content == "명령어":
        await message.channel.send("hi, Hi,bye, 숫자, 해말아, ㅅㅂ, 시발, 아, 아니, 아., 닥쳐, 넌 닥쳐, ㄷㅊ, 어쩌라고, 재배맨, 송강, 마크툽, 건터, 가위바위보")
    
    if message.content == "Hi":
        await message.channel.send("hi")
        
    if message.content == "김범준":
        await message.channel.send("ㅄ")
        
    if message.content == "bye":
        await message.channel.send("비와이")
        
    if message.content == "마크툽":
        await message.channel.send("대한민국의 가수이자 작사가, 작곡가[4], 싱어송라이터, 음악 프로듀서이다.2011년 발표한 앨범 <하울링(Howling)>으로 데뷔했다. 음악을 좋아하는 아버지의 영향을 많이 받았다고 한다. 집에 아버지가 모아놓은 LP판만 해도 1만 장 정도. 대학에선 실용음악과에 진학해 화성학과 보컬을 전공했다. 군 제대 후 본격적으로 곡을 만들어 앨범 <하울링(Howling)>과 <이너 비전(Inner vision)>을 발표한다. 마크툽은 두 앨범이 성적은 저조했지만 그때 프로듀서로서 기술적 틀과 제작 과정을 밟아가는 기반을 만들었던 것 같다고 말했다. 그는 시간이 지나, 2014년 이후 지속적으로 싱글 앨범들을 발표하면서 가요계에서 커리어를 쌓기 시작한다. '비 올 때 듣기 좋은 노래', '고백할 때 부르는 노래' 등으로 그의 노래들은 아날로그 감성을 담은 가사와 트렌디한 멜로디로 사랑받기 시작했다. 주로 감성적인 발라드·R&B 장르의 곡들이다.그러다 2014년 8월 발표한 노래 'Marry me'의 SNS를 통한 역주행으로 한순간에 대중들의 관심을 받게 된다. 'Marry me'는 2017년 멜론 연간차트 5위에 오르는 성과를 낸다. 이어 2019년 '오늘도 빛나는 너에게' 로 대히트를 치며 인지도를 높였다.2019년 12월 30일에 발표한 싱글 음원 마음이 말하는 행복도 차트 10위권까지 들어오면서 더욱 알려지게 되었고 최근에는 별을 담은 시, ‘비로소 너에게 도착했다(Full Bloom)’ 등의 곡들도 전부 히트 시키며 음원강자로서의 입지를 굳건히 했다.여기서 놀라운것은 메이저 회사의 지원 없이 모든 앨범의 기획/제작부터 곡을 만들기까지 오직 본인의 능력으로 일구어낸 결과물 이라는 것. (그만큼 수입도 다른 음원강자들에 비해 더 어마어마 한것으로 추정..)마크툽이 지금까지 보여준 진성 최고음은 3옥타브 도 (C5)[5][6]로 충분히 넓은 음역대와 사기급 음색으로 이미 엄청난 무기를 갖고 있지만, 마크툽의 진짜 무기는 믹스보이스와 가성이다. 오늘도 빛나는 너에게 3절 중간에서는 애드리브로 3옥타브 솔♯(G♯5)의 고음을 내고 라이브를 할 때에는 원래 이라온의 파트인 3옥타브 레 # (D # 5)[7]의 고음을 믹스보이스를 이용해서 깔끔하게 소화한다. 이것도 엄청 높은 음이지만 그의 고음 포텐은 여기서 끝이 아니었다. 마음이 말하는 행복에서는 3옥타브 라(A5), 그리고 바로 다음 신곡 너를 그린 우주에서는 4옥타브 도♯(C♯6)의 상당한 고음을 정말 깔끔한 휘슬 레지스터로 소화한다. 2021년 3월 7일 발매된 비로소 너에게 도착했다에서는 진성으로 3옥타브 도(C5)의 고음과 후반부 애드리브에선 가성 4옥타브 레(D6)라는 극고음을 낸다. 심지어 그 상당한 고음을 마치 음역대가 더 남은 것처럼 쉽게 찍어버리기 때문에 음역대가 현재까지 알려진것보다 더 높은 것으로 보인다. 만약 휘슬을 제대로 쓴다면 5옥타브 이상 낼 수도 있을 것이다.4옥타브 초반대도 저렇게 쉽게 낼 정도면 웬만한 콜로라투라 소프라노 음역대도 소화 가능할 정도이다.이외에도 성량이 굉장히 큰 편이다. 이라온이 진성으로 부를 때 옆에서 가성 애드리브를 하는데도 이라온의 목소리가 묻힐정도.")
        
    if message.content == "송강":
        await message.channel.send("넷플릭스 <스위트홈>으로 이름을 알린 대한민국의 배우이다.고등학교 졸업 후에도 하고 싶은 일이 아무것도 없었다고 한다. 친구들은 대학교에 갔는데 자신만 가지 않아 마음이 허했다고. 인테리어나, 설계도를 보는 걸 좋아해서 이쪽으로 나가면 어떨까 싶었지만[12]공부에 대한 장벽을 느끼고 포기한 상태에서 1년 정도 시간을 보내다가 우연히 타이타닉을 보고 레오나르도 디카프리오의 눈빛이 너무 좋아, 그 눈빛에 반해서 막연히 연기를 하고 싶다는 마음이 들었다고 한다. # 연기의 꿈을 갖고 입시를 준비하게 되고 처음 연기학원에 등록하고 계속할 수 있을지 고민도 했지만 '한 달만 채우자'라는 마음으로 버텼다고 한다. 그런데 하다 보니 차츰 좋아지고 익숙해져서 끝까지 해 봐야겠다고 마음이 들었다고 한다.그 후 회사를 찾으면서 나무엑터스와 매니지먼트 계약을 하게 됐고, 자연스럽게 연예계로 들어오게 되었다. 2017년 tvN 드라마 《그녀는 거짓말을 너무 사랑해》에서 백진우 역할로 데뷔했다. 극 중 백진우는 소림(조이)의 절친이자 소림과 함께 밴드 머시앤코를 결성하는 고등학생으로 늘 티격태격하는 소림을 짝사랑하지만, 마음을 고백하지 못해 가슴앓이를 하는 인물. # 같은 해에는 MBC 드라마 《밥상 차리는 남자》에 김우주 역할로 주말드라마에 첫 출연했다. 송강이 연기한 김우주는 정화영(이일화)의 둘째 아들이자 정태양(온주완)의 이부동생. 덩치는 운동선수처럼 우람하지만, 성격은 내성적이고 참한 고3 수험생으로 유도부 부원인 동시에 셀프 네일아트와 뜨개질이라는 반전 취미를 가진 인물으로, 실제로도 185cm의 큰 키와 넓은 어깨를 지닌 독보적인 피지컬과 맞아 떨어진 역할이라 볼 수 있겠다. 이후 2018년 2월 송강은 웹드라마 《뷰티풀 뱀파이어》에 정연주와 남녀주인공으로 캐스팅되었다. # 이 드라마는 KBS 1TV '독립영화관'을 통해서도 방영 되었다. 연기 외에도 JTBC 웹예능 《이옵빠몰까 시즌 2》에 정건주, 강훈, 이현준와 출연하였고,[13] 11월에는 SBS 예능 프로그램 《미추리 8-1000》에 고정 출연했고, 2019년 2월에 방송된 시즌 2에도 출연했다.  또한 SBS 인기가요의 MC에도 발탁되며 바쁜 나날을 보냈다. 2019년 송강은 tvN 《악마가 너의 이름을 부를 때》에서 정경호가 연기하는 하립의 신예 어시스턴트로 못 다루는 악기가 없는 음악 천재이자 꿈을 좇아 한국으로 가출을 감행한 4차원 소년 루카 역할을 맡아 연기했다. 같은 해 8월에 공개된 넷플릭스 오리지널 드라마 《좋아하면 울리는》에서 초절정 인기 모델 황선오 역할을 맡아 김조조(김소현)에게 거침없는 직진하는 매력을 뽐내며 국내뿐만 아니라 해외 팬들에게도 점차 주목을 받게 되었다.  연출을 맡은 이나정 감독은 송강을 캐스팅한 이유에 대해 처음에 보고 모델 혹은 아이돌인 줄 알았다. 그런데 배우만 준비했다더라. 매 오디션마다 모습이 다양하게 변했는데 자신감 넘치고 해맑은 모습에 매력을 느꼈다라고 말했다.  시즌 2도 2020년 초에 촬영을 마쳤으며 2021년 3월 12일에 공개가 되었다.그리고 곧바로 넷플릭스 오리지널 드라마 《스위트홈》에 캐스팅이 됐다. 연달아 넷플릭스에서만 두 작품으로, 넷플릭스의 아들이라는 수식어에 대해서는 너무 감사한 일이다. 앞으로도 더 좋은 수식어들을 얻기 위해 더 많이 노력해야겠다고 생각한다.라고 답했다.")
    if message.content == "재배맨":
        await message.channel.send("드래곤볼에서 사이어인의 과학자가 만든 전투생물.한국 해적판 및 비디오 더빙판 이름은 사이버맨.SBS 방영 당시는 '베지맨'이었다.성우는 각각 후루카와 토시오, 스즈오키 히로타카, 후루야 토오루.스파킹 시리즈에서는 누마타 유스케.작은 병 안에 씨앗을 휴대하고 다니다가 땅에 잘 심고 병에 같이 동봉된 액체를 심은 씨앗 위에 뿌려주면 순식간에 무럭무럭 자라서 인간형 괴물이 된다. 이 괴물을 '재배맨'이라고 부른다. 이름이나 생성 방법에서 알 수 있듯이 '재배하다'의 그 재배가 맞다. 사이언인들의 작명 자체가 채소에서 따온 것인데, 재배맨 또한 그 영향을 받은 듯하다. 작중 행적선봉으로 나온 놈이 천진반에게 패배했다가 일어났지만 베지터가 가차없이 죽여버렸다. 내퍼가 왜 그러냐고 하자, 베지터는 '방심하던 녀석은 더 이상 필요가 없어'라는 말을 했는데 남은 재배맨들은 이 말에 겁먹은 얼굴을 했다. 그리고 야무치가 두 번째 재배맨을 상대로 잘 싸웠으나, 놈이 에네르기파에 맞아 죽은 줄 알고 방심해서 아직 죽지 않았던 재배맨의 자폭에 사망한다.천진반과 야무치의 일격에 거의 전투불능이 되긴 했지만 죽지는 않은 것으로 보아서, 의외로 생명력은 Z전사들의 예상보다 강했던 것 같다. 원작에서는 내퍼가 사용한 재배맨들로 단 한 번 나왔으며 야무치 사후 크리링의 확산 에네르기파로 거의 전멸했다. 한 놈이 살아남아 손오반에게 덤벼들긴 했는데 피콜로에게 펀치를 맞고 공중으로 던져져 입에서 발사된 광선에 맞아 해골만 남는, 말 그대로 처참한 최후를 맞았다.버독 TV 스페셜 단 한명의 최종결전에선 베지터의 연습용 상대로 강화한 재배맨 여섯 놈이 단번에 쓸려나갔고 극장판 '세상에서 제일 강한 자!'에서는 재배맨 업그레이드 버전처럼 보이는 바이오맨이라는 개체들도 나온다.드래곤볼 GT에서는 지옥에서 대량으로 발생했으며 오천과 트랭크스가 크게 기분 나빠했지만 우부에 의해 퇴치된다.심을 때의 토지의 영양 상태에 따라 전투력이 변화한다. 지구에서는 토양이 좋기 때문에 전투력 1,200[4]의 재배맨들이 나왔다. 슈퍼까지 나온 현재로썬 그저 잡몹 수준이지만 당시 저 정도 전투력이면 무인편 기준 상당한 강자였던 타오파이파이(110), 학선인(120), 무천도사(139), 피콜로 대마왕(260)보다 훨씬 강한 수준이고, 챠오즈나 손오반은 정면승부로는 절대 못 이기며 피콜로와 손오공조차 고전했던 라데츠(1,500)에 조금 못 미치는 수준이다.[5] 실제로 전투력 1,500을 찍은 크리링과 오반 이 둘만으로 나메크성에서 프리저 군과 교전할 때 상급전사 이상만 안 나오면 그외 잡졸들을 상대로는 무쌍 찍을 수 있던 수준이었다. 제작공정에 좀 더 특수한 공정을 거치는 것인지 아니면 토양 차이인지는 모르겠으나 지구산 재배맨도 제일 좋은 상태는 아니라고 한다.머리에서 엄청난 위력의 용해액을 내뿜을 수 있으며, 눈에 전혀 보이지 않고 기의 움직임을 느껴서만 볼 수 있을 정도의 초고속이동을 할 수 있다. 게다가 방어력도 상당해 당시 전투력 1,480이었던 야무치의 에네르기파[6]를 정통으로 맞고도 죽지 않았다. 마지막으로 상당한 피해를 받았을 때는 적에게 달라붙어 자폭을 하는데 자신보다 전투력이 높은 야무치를 죽일 정도로 어마어마한 위력을 자랑한다.")
        
    if message.content == "hi":
        await message.channel.send("에이치아이")

    if message.content == "숫자":
        a = random.randrange(1000,10000)
        
        await message.channel.send(a)
        
    if message.content == "해말아":
        do = random.randint(0,1)
        if do == 0:
            answer = "해"
        if do == 1:
            answer = "말아"
        await message.channel.send(answer)
        
    if message.content == "ㅅㅂ":
        await message.channel.send("욕은나빠용")
        
    if message.content == "시발":
        await message.channel.send("욕은나빠용")
        
    if message.content == "아":
        await message.channel.send("ㅋㅋ화났죠?")
        
    if message.content == "아니":
        await message.channel.send("화내지마!!")
        
    if message.content == "아.":
        await message.channel.send("참아")
        
    if message.content == "닥쳐":
        await message.channel.send("엥")
        
    if message.content == "넌 닥쳐":
        await message.channel.send("엥")
        
    if message.content == "ㄷㅊ":
        await message.channel.send("엥")
        
    if message.content == "어쩌라고":
        await message.channel.send("빠큐")
        
    if message.content == "가위바위보":
        await message.channel.send("33333")
        time.sleep(1)
        await message.channel.send("22222")
        time.sleep(1)
        await message.channel.send("11111")
        
        
    if message.content == "건터":
        await message.channel.send("어드벤처 타임에 등장하는 펭귄이다. 성우는 얼음 대왕과 같은 톰 케니. 얼음 대왕과 늘 함께 다니는 펭귄. 병을 깨트리는 것을 좋아한다. 순수한 얼굴로 나쁜 행동을 하는 것이 특기다. 예로 수면 가스 통을 아이스킹의 케이크에 끼워넣는다던지...마셀린의 아버지인 헌슨 애버디어의 말에 따르면 모든 역사 속 괴물들 보다도 훨씬 사악한 영혼을 가지고 있다고 했다. 영혼을 내놓으라는 헌슨의 말에 되려 헌슨의 영혼을 내놓으라고 패기있게 대답하는 것부터, 헌슨의 영혼 흡수를 무시하고 역으로 뺨싸대기를 후려갈긴 유일한 캐릭터라서 권터가 리치보다 훨씬 강력한 무언가가 아니냐 하는 흑막론이 존재했다. 시즌4 24화 'Reign of gunthers' 편에서 데모닉 위싱 아이를 목에 걸고 그 사악함을 과시했는데, 아이스킹이 분무기를 들고 나쁘다며 쏘니까 불만을 표시하며 벗어던졌다. 참고로 아이스킹은 위에 언급된 일화에서 배웠을, 권터가 매직 아이템을 가질 경우 큰일이 벌어진다는 교훈은 홀라당 까먹었는지, 훗날 플레임 프린세스와의 전투로 파괴된 얼음왕국을 재건할 때 권터에게 자신의 마법왕관을 맡겨 마법을 부리게 했다. 그리고 권터가 만들어낸 눈 생명체에게 된통 당하고 말았다.아이스킹과는 애완동물과 주인보다는 아빠와 아들같은 관계이다. 아이스킹에게 빗질을 해달라고도 하며 잘못을 했을 때 벌로 구석에 서있고, 결정적으로 아이스킹이 권터에게 말할때 자신을 아빠라고 지칭한다. 그리고 다른 펭귄들에 비해 엄하게 대하고 있다. 가령 아이스킹이 기뻐서 눈물이 나올때 다른 펭귄들이 눈물을 먹게 허락해도 권터는 너 요즘 짜게 먹잖아!라며 쳐낸다... 참고로 권터에게도 자식이 있는데 뜬금없게도 핑크색 고양이다. 데모닉 위싱 아이를 들고 폭주할 때도 애를 업고 있는 걸 보면 자신이 어머니라는 자각은 있는 것 같다. .아이스 킹이 얼음 왕국에 사는 모든 펭귄들을 권터라 부르는 것이 아니냐는 의문이 있었으나 시즌4 9화에서 펭귄들을 부를 때 다른 이름으로 부르는 장면이 나오면서 '권터'라는 펭귄은 한 마리 뿐이란 게 밝혀졌다. 근데 시즌3 19화에서 다른 펭귄들도 권터라고 부르는 걸 보면 대명사로도 사용되는 것 같다. 사실 권터는 세 마리다. 시즌 4 9화를 보면 권터만 3번 부르는 걸 볼 수 있다. 시즌 5 14화에서 마셀린을 권터라고 부르는 장면이 나왔다. 아무래도 권터를 딸처럼 여기는 것도 어린 마셀린과의 기억이 투영되어서 나오는 것일지도 모른다. 별 중요한 건 아니지만 당시 사이먼은 47살 마셀린은 7살이었다.시즌 6 evergreen에피소드에서 권터라는 이름을 가진 공룡소년과 함께 아이스킹의 왕관의 기원이 나오는데 얼음 마법사 에버그린의 제자인 공룡소년의 이름이 권터다! 원래 이 왕관은 사용자의 모든 소원이든 들어주는 왕관인데 공룡 권터가 '자신도 에버그린처럼 되고싶다' 라는 소원을 빌어서 그 왕관이 '에버그린으로 되는 왕관'이 된 것인데, 에버그린이 가지고 있는 얼음 능력과 무한한 수명을 얻게되지만 부작용으로 반쯤 미치고 자신의 자식 혹은 제자 정도의 이미지를 가진 사람에게 똑같이 '권터'라고 부르게 되는 부작용이 있는 것 같다.따라서 아이스 킹이 자신의 펭귄에게 '권터'라는 이름을 붙여준 것은 이 왕관에 의한 영향인 것으로 밝혀졌다.")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
