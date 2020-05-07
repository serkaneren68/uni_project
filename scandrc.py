
import os
numberlist = []
stringlist = []
dosyalar = os.listdir()
def capitalize(line):
    line = line.replace("_"," ")
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))

def upper(x):
    x = x.replace("_"," ")
    return x.title()


def finddot(x):
    index = x.find(".")
    return x[4:index]


for i in dosyalar:
    numberlist.append(i[0:3])
    stringlist.append(capitalize(finddot(i)))




string1 = """<!-- wp:spacer {"height":20} -->
<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p><strong>"""

deger1= 0

string2 ="""</strong> taban puanları ve başarı sıralamalarını bu sayfada bulabilirsiniz. Sınav Sayacı, siz değerli kullanıcılarımız için <strong>2020 yılının güncel """

deger2 = 0

string3 = """ taban puanlarını ve taban başarı sıralamalarını</strong> tamamen YÖK Atlas ve ÖSYM verilerinden baz alarak hazırladı.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"very-dark-gray","customFontSize":18} -->
<p style="font-size:18px" class="has-text-color has-very-dark-gray-color">✩ Aşağıya eklemiş olduğumuz taban puanları ve başarı sıralamaları tablomuz tamamıyla ÖSYM'nin verilerinden elde edilmiştir ve günceldir.Veriler ÖSYM'ye bağlı olarak düzenli bir şekilde senkronize edilecektir.Tercihlerinizi yaparken çekinmeden yararlanabilirsiniz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"vivid-red"} -->
<p class="has-text-color has-vivid-red-color"><strong>✪ Tablonun sağ üst tarafındaki "Bul" alanına aradığınız üniversitenin adını yazarak hızlı bir şekilde sonuca ulaşabilirsiniz. ↴</strong></p>
<!-- /wp:paragraph -->

<!-- wp:html -->[table id="""
deger3 = 0

string4 = """ /]<!-- /wp:html -->

<!-- wp:spacer {"height":20} -->
<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:coblocks/row {"paddingSize":"small","marginSize":"small","backgroundColor":"very-dark-gray","columns":2,"layout":"50-50","gutter":"small","coblocks":{"id":"32316437374"}} -->
<div class="wp-block-coblocks-row coblocks-row-32316437374" data-columns="2" data-layout="50-50"><div class="wp-block-coblocks-row__inner has-very-dark-gray-background-color has-background has-small-gutter has-padding has-small-padding has-margin has-small-margin is-stacked-on-mobile"><!-- wp:coblocks/column {"width":"51.27","coblocks":{"id":"3231643940"}} -->
<div class="wp-block-coblocks-column coblocks-column-3231643940" style="width:51.27%"><div class="wp-block-coblocks-column__inner has-no-padding has-no-margin"><!-- wp:html -->
<button type="button" a="" class="btn btn-danger btn-lg btn-block"><a style="text-decoration: none;" href="https://sinavsayaci.com/4-yillik-bolumlerin-taban-puanlari-ve-basari-siralamalari/"><font face="tahoma" size="5" color="black"> 4 yıllık bölümlerin taban puanlarına ulaşmak için tıklayınız</font></a></button>
<!-- /wp:html --></div></div>
<!-- /wp:coblocks/column -->

<!-- wp:coblocks/column {"width":"48.55","coblocks":{"id":"3231643977"}} -->
<div class="wp-block-coblocks-column coblocks-column-3231643977" style="width:48.55%"><div class="wp-block-coblocks-column__inner has-no-padding has-no-margin"><!-- wp:html -->
<button type="button" class="btn btn-success btn-lg btn-block"><a style="text-decoration: none;" href="https://sinavsayaci.com/2-yillik-bolumlerin-taban-puanlari-ve-basari-siralamalari/"><font face="tahoma" size="5" color="black"> 2 yıllık bölümlerin taban puanlarına ulaşmak için tıklayınız</font></a></button>
<!-- /wp:html --></div></div>
<!-- /wp:coblocks/column --></div></div>
<!-- /wp:coblocks/row -->"""

for i in range(424):
    allofthis =(string1+stringlist[i]+string2+stringlist[i]+string3+numberlist[i]+string4)
    dosya = open("{}.txt".format(stringlist[i]),"w" )
    dosya.write(allofthis)
    dosya.close()
    print("\n\n\n\n\n")
