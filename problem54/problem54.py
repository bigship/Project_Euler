# project euler problem 54
# http://projecteuler.net/problem=54

# Texas Holden winning hand

card_value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, 
'8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }

ranking = {'high card':1, 'one pair':2,
'two pairs':3, 'three kind':4, 'straight':5,
'flush':6, 'full house':7, 'four kind':8,
'straight flush':9, 'royal flush':10}

def get_playerhands():
    with open('poker.txt', 'r') as f:
        game_round = f.read().split('\n')
        for hands in game_round:
            first_player = hands[0:14]
            second_player = hands[15:]
            yield first_player, second_player

def hand_ranking(hand):
    if is_royal_flush(hand):
        return ranking['royal flush']
    elif is_straight_flush(hand):
        return ranking['straight flush']
    elif is_straight(hand):
        return ranking['straight']
    elif is_flush(hand):
        return ranking['flush'] 

    four_kind = [1, 4, 4, 4, 4]
    three_kind = [1, 1, 3, 3, 3]
    full_house = [2, 2, 3, 3, 3]
    two_pair = [1, 2, 2, 2, 2]
    one_pair = [1, 1, 1, 2, 2]
    card = [hand[i] for i in xrange(0, 10) if i % 2 == 0]
    show_up_cnt = sorted([card.count(card[i]) for i in xrange(0, 5)])
    if show_up_cnt == four_kind:
        return ranking['four kind']
    elif show_up_cnt == three_kind:
        return ranking['three kind']
    elif show_up_cnt == full_house:
        return ranking['full house']
    elif show_up_cnt == two_pair:
        return ranking['two pairs']
    elif show_up_cnt == one_pair:
        return ranking['one pair']
    else:
        return ranking['high card']

def is_flush(hand):
    return hand[1] == hand[3] == hand[5] == hand[7] == hand[9]

def is_straight(hand):
    t = sorted([card_value[hand[i]] for i in xrange(0, 10) if i % 2 == 0])
    return t[0] + 1 == t[1] and t[1] + 1 == t[2] and \
    t[2] + 1 == t[3] and t[3] + 1 == t[4]


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)

def is_royal_flush(hand):
    tmp = [hand[0], hand[2], hand[4], hand[6], hand[8]]
    if is_straight_flush(hand) and ''.join(sorted(tmp)) == 'TJQKA': 
        return True
    else:
        return False

def get_four_kind_card(cards):
    f = None
    for i in cards:
        if cards.count(i) == 4:
            f = card_value[i]
            break
    return f

def get_full_house_card(cards):
    t = None
    for i in cards:
        if cards.count(i) == 3:
            t = card_value[i]
            break
    return t

def get_three_kind_card(cards):
    a = None
    for i in cards:
        if cards.count(i) == 3:
            a = card_value[i]
    return a

def get_two_pair_card(cards):
    a, b, c = None, None, None
    for i in cards:
        if cards.count(i) == 2:
            if a == None:
                a = i
            elif a != i:
                b = i
        else:
            c = i
    return card_value[a], card_value[b], card_value[c]

def get_one_pair_card(cards):
    a, b, c, d = None, None, None, None
    for i in cards:
        if cards.count(i) == 2:
            a = card_value[i]
        elif cards.count(i) == 1:
            if b == None:
                b = card_value[i]
            elif b != None and c == None:
                c = card_value[i]
            elif b != None and c != None:
                d = card_value[i]
    return a, b, c, d

def get_all_cards(cards):
    return [card_value[x] for x in cards]

def compare_all_cards(s1, s2):
    for i in s1:
        if i in s2:
            s1.remove(i)
            s2.remove(i)
    return max(s1) > max(s2)

                
if __name__ == '__main__':
    wins = 0
    for first_player, second_player in get_playerhands():
        rank1 = hand_ranking(first_player.replace(' ', ''))
        rank2 = hand_ranking(second_player.replace(' ', ''))
        if rank1 > rank2:
            wins += 1
            
        elif rank1 == rank2:
            cards1 = [first_player.replace(' ', '')[i] for i in xrange(0, 10) if i % 2 == 0]
            cards2 = [second_player.replace(' ', '')[i] for i in xrange(0, 10) if i % 2 == 0]           
            
            if rank1 == ranking['straight flush'] or rank1 == ranking['straight']:
                if max(cards1) > max(cards2):
                    wins += 1
                    
            elif rank1 == ranking['four kind']:
                f1 = get_four_kind_card(cards1)
                f2 = get_four_kind_card(cards2)
                if f1 > f2:
                    wins += 1
                    
            elif rank1 == ranking['full house']:
                t1 = get_full_house_card(cards1)
                t2 = get_full_house_card(cards2)
                if t1 > t2:
                    wins += 1
                    
            elif rank1 == ranking['three kind']:
                q1 = get_three_kind_card(cards1)
                q2 = get_three_kind_card(cards2)
                if q1 > q2:
                    wins += 1
                    
            elif rank1 == ranking['two pairs']:
                a1, b1, c1 = get_two_pair_card(cards1)
                a2, b2, c2 = get_two_pair_card(cards2)
                if max(a1, b1) > max(a2, b2):
                    wins += 1
                elif max(a1, b1) == max(a2, b2):
                    if min(a1, b1) > min(a2, b2):
                        wins += 1
                elif a1 == a2 and b1 == b2:
                    if c1 > c2:
                        wins += 1
                        
            elif rank1 == ranking['one pair']:
                p1, p2, p3, p4 = get_one_pair_card(cards1)
                p5, p6, p7, p8 = get_one_pair_card(cards2)
                if p1 > p5:
                    wins += 1
                elif p1 == p5 and max(p2, p3, p4) > max(p6, p7, p8):
                    wins += 1
                    
            elif rank1 == ranking['flush']:
                x = get_all_cards(cards1)
                y = get_all_cards(cards2)
                if compare_all_cards(x, y):
                    wins += 1
                    
            elif rank1 == ranking['high card']:
                x = get_all_cards(cards1)
                y = get_all_cards(cards2)
                if compare_all_cards(x, y):
                    wins += 1
    print wins
