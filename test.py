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

if beurt = groen:
  verzekeringen_groen = verzekeringen(groen, salarissen)