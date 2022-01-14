#Program that reads a value in meters and displays it converted into kilometer km, hectometer hm, decameter dam, decimeter dm , centimeter cm and millimeter mm.
print('====== DEFIANCE 008 ======')
m = float(input('A distance in meters: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('The measurement of {} meters corresponds to: \n {:.3f}km \n {:.2f}hm \n {:.1f}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))
