def distance(vec1, vec2):
    # yig'indi bo'lgani uchun
    # boshlang'ich qiymat 0 ga teng
    s = 0
    # sanash uchun
    i = 0
    while i < 784:
        # ikki rasm o'rtasidagi farq
        diff = vec1[i] - vec2[i]
        # masofa manifiy bo'lmasligi
        # uchun uni musbatga aylantiramiz
        abs_dist = abs(diff)
        # jami yig'indiga qo'shamiz
        s = s + abs_dist
        # sanashni oshirish
        i = i + 1
    
    return s