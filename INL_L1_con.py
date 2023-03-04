
# coding: utf-8

# In[3]:


import morfeusz2
morf = morfeusz2.Morfeusz(generate=False, expand_tags=True)
text = "Według bieżących ustaleń, początkowo księga miała 272 strony w 17 librach po 16 stron każda. Do dziś zachowało się 240 welinowych stron, a luki w numeracji stron (która zdaje się starsza niż sam tekst) świadczą o tym, że kilku stron brakowało, zanim Wojnicz wszedł w posiadanie księgi. Kontury cyfr wykonano gęsim piórem, a kolorowa farba została naniesiona na cyfry (odrobinę prymitywnie) prawdopodobnie w późniejszym okresie. Istnieją niezbite dowody, że w bliżej nieznanej przeszłości zmieniono kolejność stron Całość została napisana od lewej do prawej strony, z nieco nierównym prawym marginesem. Dłuższe ustępy podzielono na akapity, niekiedy z punktorami po lewej stronie, jednak w manuskrypcie nie ma wyraźnej interpunkcji. Dukt (czyli tempo, staranność i stopień nachylenia, z jakim litery zostały napisane) sugeruje, że skryba rozumiał, co pisze. Manuskrypt nie sprawia wrażenia, że litery miały być wymierzone przed naniesieniem ich na welin (różnią się nieco od siebie, co utrudnia odczyt komputerowy). Tekst składa się z ponad 170 tys. glifów, zazwyczaj oddzielonych wąskimi odstępami. Większość glifów została napisana przy pomocy jednego lub dwóch pociągnięć ręki. Mimo sporów dotyczących odrębności niektórych glifów, alfabet składa się z 20 lub 30 znaków i wystarczyłby do napisania praktycznie całego tekstu. Wyjątkiem jest kilkadziesiąt rzadkich znaków pojawiających się raz lub dwa. Luki dzielą tekst na około 35 tys. „słów” różnej długości, przy czym „słowa” te wydają się zgodne z pewnego rodzaju zasadami fonetycznymi i gramatycznymi, np. pewne znaki muszą się pojawić w każdym słowie (jak samogłoski w języku angielskim lub łacińskim), z kolei inne nigdy nie następują po sobie, niektóre mogą być podwajane, a inne nie. Analiza statystyczna tekstu ukazuje schematy podobne do tych w językach naturalnych. Przykładem może być częstotliwość występowania słów, która jest zgodna z prawem Zipfa. Również entropia słowa podobna jest do tej w języku łacińskim lub angielskim. Pewne słowa pojawiają się tylko w niektórych fragmentach lub tylko na kilku stronach, inne z kolei są obecne w całym tekście. Jest bardzo niewiele powtórzeń wśród ponad tysiąca „etykiet” dołączonych do ilustracji. W sekcji zielarskiej pierwsze słowo na każdej stronie występuje tylko i wyłącznie tam, być może jest to nazwa omawianej rośliny. Z drugiej strony język manuskryptu Wojnicza jest niepodobny do języków europejskich pod kilkoma względami. Po pierwsze, nie ma w nim praktycznie żadnych słów składających się z więcej niż dziesięciu znaków. Niewiele jest też słów jedno- lub dwuliterowych. Rozkład liter w słowie jest też specyficzny. Niektóre znaki występują tylko na początku słowa, inne tylko na końcu, a jeszcze inne zawsze w środku. Jest to fenomen spotykany w alfabetach semickich, a nie w łacinie czy cyrylicy (z wyjątkiem greckich liter beta i sigma). Manuskrypt zawiera więcej powtórzeń niż typowe języki europejskie. Niekiedy to samo „słowo” pojawia się nawet trzy razy z rzędu. Również wyrazy, które różnią się tylko jedną literą, powtarzają się niezwykle często. Słów, które przypominają pismo łacińskie, jest w manuskrypcie niewiele. Cztery linijki tekstu na ostatniej stronie, poza dwoma wyrazami, zostały napisane (nieco zniekształconymi) literami łacińskimi. Pismo przypomina europejskie z XV wieku, jednak słowa nie mają sensu w żadnym języku. Serie diagramów w sekcji astronomicznej zawierają nazwy dziesięciu miesięcy (od marca do grudnia) napisane alfabetem łacińskim z pisownią wskazującą na średniowieczne języki Francji lub Półwyspu Iberyjskiego[8]. Nie wiadomo jednak, czy te fragmenty pisane literami łacińskimi były częścią oryginalnego tekstu, czy zostały dodane w późniejszym czasie."
import os
os.getcwd()
import subprocess
print(subprocess.check_output('C:\\Users\\s10552\\Desktop\\INL\\cki\\concraft-dag2-pl.exe --help', shell=True))
def edge4concraft(edge):
    i, j, (orth, base, tag, posp, kwal) = edge
    return u'{}\t{}\t{}\t{}\t{}\t\t\t0.0000\t\t'.format(i, j, orth, base, tag)

concraft_input = '\n'.join(map(edge4concraft, morf.analyse(text)))
print('INPUT FOR CONCRAFT:\n')
print(concraft_input)
print('\n[END INPUT FOR CONCRAFT]')

input_file = 'input.dag'
with open(input_file, encoding='utf-8', mode='w') as f:
    f.write(concraft_input)

    

