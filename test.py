def verzekeringen(beurt, salarissen):
  if posities[huidige_speler_beurt] in verzekeringPositie:
    if posities[huidige_speler_beurt] == 4:
      return " levens verzekering"
      salarissen[huidige_speler_beurt] -= 750
      return salarissen
      print("Speler", huidige_speler_beurt, " heeft een levens verzekering en 750 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
    elif posities[huidige_speler_beurt] == 11:
      verzekeringen[huidige_speler_beurt] + (" reis verzekering")
      salarissen[huidige_speler_beurt] -= 500
      print("Speler", huidige_speler_beurt, " heeft een reis verzekering en 500 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
    elif posities[huidige_speler_beurt] == 20:
      verzekeringen[huidige_speler_beurt] + (" Auto verzekering")
      salarissen[huidige_speler_beurt] -= 1000
      print("Speler", huidige_speler_beurt, " heeft een auto verzekering en 1000 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
    elif posities[huidige_speler_beurt] == 26:
      verzekeringen[huidige_speler_beurt] + (" Brand verzekering")
      salarissen[huidige_speler_beurt] -= 1200
      print("Speler", huidige_speler_beurt, " heeft een brand verzekering en 1200 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
    elif posities[huidige_speler_beurt] == 33:
      verzekeringen[huidige_speler_beurt] + (" inboedel verzekering")
      salarissen[huidige_speler_beurt] -= 1350
      print("Speler", huidige_speler_beurt, " heeft een inboedel verekering en 1350 euro minder. ", "Nieuwe salaris: ", + int(saalarissen[huidige_speler_beurt]))
    elif posities[huidige_speler_beurt] == 38:
      verzekeringen[huidige_speler_beurt] + (" overlijdensrisico verzekering")
      salarissen[huidige_speler_beurt] -= 680
      print("Speler", huidige_speler_beurt, " heeft een overlijdings verzekering en 680 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))


#main


 if huidige_speler_beurt == 0:
   beurt = "groen"
   print("Beurt speler", beurt)
  
 elif huidige_speler_beurt == 1:
   beurt = "blauw"
   prin("Beurt speler", beurt)

 elif huidige_speler_beurt == 2:
   beurt = "geel"
   print( "Beurt speler", beurt)

if beurt == groen:
  verzekeringen_groen = verzekeringen(groen)

elif beurt == blauw:
  verzekeringen_blauw = verzekeringen(blauw)

elif beurt == geel:
  verzekeringen_geel = verzekeringen(geel)


def verzekeringen(beurt):
  if posities[huidige_speler_beurt] in verzekeringPositie:
    if posities[huidige_speler_beurt] == 4:
      verzekeringen.insert(beurt +1, " levens verzekering")
      salarissen[beurt] -= 750
      print("Speler", beurt, " heeft een levens verzekering en 750 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
    elif posities[huidige_speler_beurt] == 11:
      verzekeringen.insert(beurt +1, " reis verzekering")
      salarissen[beurt] -= 500
      print("Speler", beurt, " heeft een reis verzekering en 500 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
    elif posities[huidige_speler_beurt] == 20:
      verzekeringen.insert(beurt +1, " Auto verzekering")
      salarissen[beurt] -= 1000
      print("Speler", beurt, " heeft een auto verzekering en 1000 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
    elif posities[huidige_speler_beurt] == 26:
      verzekeringen.insert(beurt +1, " Brand verzekering")
      salarissen[beurt] -= 1200
      print("Speler", beurt, " heeft een brand verzekering en 1200 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
    elif posities[huidige_speler_beurt] == 33:
      verzekeringen.insert(beurt +1, " inboedel verzekering")
      salarissen[beurt] -= 1350
      print("Speler", beurt, " heeft een inboedel verekering en 1350 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
    elif posities[huidige_speler_beurt] == 38:
      verzekeringen.insert(beurt +1, " overlijdensrisico verzekering")
      salarissen[beurt] -= 680
      print("Speler", beurt, " heeft een overlijdens verzekering en 680 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt])
      
    return verzekeringen
    






verzekeringen_groen = ["verzekeringen Groen: "]
verzekeringen_blauw = ["verzekeringen Blauw: "]
verzekeringen_geel = ["verzekeringen Geel: "]



verzekeringen = ["Verzekeringen Groen: ", "Verzekeringen Blauw: ", "Verzekeringen Geel: "]


if beurt == 0













      def verzekering(beurt):
        if posities[beurt] in verzekeringPositie:
          if posities[beurt] == 4:
            verzekeringen.insert(beurt +1, " levens verzekering")
            salarissen[beurt] -= 750
            print("Speler", beurt, " heeft een levens verzekering en 750 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
          elif posities[beurt] == 11:
            verzekeringen[beurt] + (" reis verzekering")
            salarissen[beurt] -= 500
            print("Speler", beurt, " heeft een reis verzekering en 500 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
          elif posities[beurt] == 20:
            verzekeringen[beurt] + (" Auto verzekering")
            salarissen[beurt] -= 1000
            print("Speler", beurt, " heeft een auto verzekering en 1000 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
          elif posities[beurt] == 26:
            verzekeringen[beurt] + (" Brand verzekering")
            salarissen[beurt] -= 1200
            print("Speler", beurt, " heeft een brand verzekering en 1200 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))
          elif posities[beurt] == 33:
            verzekeringen[beurt] + (" inboedel verzekering")
            salarissen[beurt] -= 1350
            print("Speler", beurt, " heeft een inboedel verekering en 1350 euro minder. ", "Nieuwe salaris: ", + int(saalarissen[beurt]))
          elif posities[beurt] == 38:
            verzekeringen[beurt] + (" overlijdensrisico verzekering")
            salarissen[beurt] -= 680
            print("Speler", beurt, " heeft een overlijdings verzekering en 680 euro minder. ", "Nieuwe salaris: ", + int(salarissen[beurt]))














#pop-up voor de verzekeringen
if posities[huidige_speler_beurt] in verzekeringPositie:
  if posities[huidige_speler_beurt] == 4:
    verzekeringen.insert(huidige_speler_beurt +1, " levens verzekering")
    salarissen[huidige_speler_beurt] -= 750
    print("Speler", huidige_speler_beurt, " heeft een levens verzekering en 750 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
  elif posities[huidige_speler_beurt] == 11:
    verzekeringen[huidige_speler_beurt] + (" reis verzekering")
    salarissen[huidige_speler_beurt] -= 500
    print("Speler", huidige_speler_beurt, " heeft een reis verzekering en 500 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
  elif posities[huidige_speler_beurt] == 20:
    verzekeringen[huidige_speler_beurt] + (" Auto verzekering")
    salarissen[huidige_speler_beurt] -= 1000
    print("Speler", huidige_speler_beurt, " heeft een auto verzekering en 1000 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
  elif posities[huidige_speler_beurt] == 26:
    verzekeringen[huidige_speler_beurt] + (" Brand verzekering")
    salarissen[huidige_speler_beurt] -= 1200
    print("Speler", huidige_speler_beurt, " heeft een brand verzekering en 1200 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))
  elif posities[huidige_speler_beurt] == 33:
    verzekeringen[huidige_speler_beurt] + (" inboedel verzekering")
    salarissen[huidige_speler_beurt] -= 1350
    print("Speler", huidige_speler_beurt, " heeft een inboedel verekering en 1350 euro minder. ", "Nieuwe salaris: ", + int(saalarissen[huidige_speler_beurt]))
  elif posities[huidige_speler_beurt] == 38:
    verzekeringen[huidige_speler_beurt] + (" overlijdensrisico verzekering")
    salarissen[huidige_speler_beurt] -= 680
    print("Speler", huidige_speler_beurt, " heeft een overlijdings verzekering en 680 euro minder. ", "Nieuwe salaris: ", + int(salarissen[huidige_speler_beurt]))