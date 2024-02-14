def bayes_compute_parameters(x, y, col):
  """
  x - o'tgatuvchi to'plam
  y - shu to'plam uchun maqsadli alomat
  col - to'plamdagi alomat indeks qaysiki biz 
  uning parametrlarini topishimiz kerak bo'lga
  """

  """
  Biz oldindan ushbu alomatda necha xil toifa borligini bilmaymiz.
  Masalan, jins alomatida ikkita bo'lsa, ma'lumoti alomatida 6 ta bor,
  yana bir boshqasida 30 ta.
  Shuning uchun avval shu alomatdagi yagona bo'lgan,
  turli xil raqamlar sonini aniqlab olamiz.
  Bu o'zgaruvchini uniques deb nomlaymiz va bu o'zgaruvchi boshida bo'sh bo'ladi.
  """

  # elementlari soni aniqlash
  n = len(x)
  uniques = []
  # sanagich
  i = 0
  # takrorlash
  while i < n:
    # biz navbatdagi alomatning qiymatini oldik
    # buning uchun birinchi uning qaysi obyekt ekanligini i indeksi orqali
    # va keyin esa col indeks orqali uning qaysi alomatligini aniqlaymiz
    current_val = x[i][col]
    # Endigi joriy element yagon elementlar ro'yxatida borligini tekshiramiz
    # agar bo'lmasa, qo'shamiz, aks holda yo'q
    # buning uchun soddalik bo'lishi maqsadida
    # in opertatoridan foydalanimiz
    # bu operator agar ro'yxat ichida biror element bo'lsa True aks holda False 
    # qaytaradi. Masalan, 3 in [4, 3, 5] => True yoki 3 in [4, 3, 5] => False
    if current_val in uniques:
      # bo'lsa hech qanday amal bajarmaymiz
      pass
    else:
      # aks holda uni qo'shib qo'yamiz
      uniques.append(current_val)
    # sanagichni oshirish
    i = i + 1
  
  """
  Keyingi qadam esa har bir toifaning
  qiymatlari necha martadan uchraganini hisoblash
  Natijalarni counts o'zgaruvchisida saqlaymiz
  va u boshida 0 qiymatlardan iborat bo'ladi
  hamda elementlar soni alomatdagi toifalar, ya'ni uniques lar soniga teng bo'ladi.
  E'tibor bering bu o'zgaruvchi ikkita bo'ladi:
  bittasi diabetga chalinganlar soni uchun ikkinchisi esa chalinmaganlar uchun
  """
  # vaqtincha bo'sh bo'ladi
  counts1 = []
  counts2 = []
  # sanagich
  i = 0
  # takrorlash to toifalar sonigacha
  while i < len(uniques):
    counts1.append(0)
    counts2.append(0)
    # sanagichni oshirish
    i = i + 1
  
  """
  Natijalarni sanishni boshlaymiz
  """
  # sanagich
  i = 0
  # takrorlash to obyektlar sonigacha
  while i < n:
    # biz navbatdagi alomatning qiymatini oldik
    # buning uchun birinchi uning qaysi obyekt ekanligini i indeksi orqali
    # va keyin esa col indeks orqali uning qaysi alomatligini aniqlaymiz
    current_val = x[i][col]
    # Indekslash hiylasi: bu hiylada biz toifalarning qiymatini 0 dan
    # boshlanadi deymiz, shunda malasan, current_val=0 chekmayadi va 
    # current_val=1 chekadini saqlaydi
    # har safar 0 ko'ranimizda chekmaydiganlar sonini oshirib qo'yamiz bittag
    # 1 ko'rsak chekadiganlarnikini
    # agar diabetga chalingan bo'lsa
    # birinchisiga
    # aks holda ikkinchisiniga
    if y[i] == 1:
      counts1[current_val] = counts1[current_val] + 1
    else:
      counts2[current_val] = counts2[current_val] + 1
    # sanagichni oshirish
    i = i + 1
  
  """
  so'ngi qadamda har bir toifaning hodisalarining
  ehtimolini hisoblaymiz av natijalarni probs o'zgaruvchisida saqlaymiz
  u boshida bo'sh bo'ladi.
  prob ham ikkita bo'ladi: diabet va diabet emas
  """
  probs1 = []
  probs2 = []
  i = 0
  while i < len(uniques):
    # har bir toifa sonini umumiy obyektlar soniga
    # bo'lib, natijani probs qo'shib qo'yamiz
    probs1.append(counts1[i] / n)
    probs2.append(counts2[i] / n)
    i = i + 1
  
  # bizga zarur bo'lgan hamma qiymatlarni hisoblab chiqidik
  # natijalarni qaytaramiz, ularni ketma-ket vergul orqali yozamiz
  return uniques, probs1, probs2