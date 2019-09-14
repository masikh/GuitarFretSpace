class GuitarFretSpaces:
    def __init__(self):
        """
        Typical lengths:
        
        24″ (610mm) Fender Jaguar, Fender Mustang
        24.5″ (622mm) Paul Reed Smith Santana Signature series
        24.75″ (628mm) most Gibson and Epiphone models
        25″ (635mm) most PRS, Carvin, and Danelectric models
        25.5″ (648mm) most Fender, Ibanez, Jackson, Kramer, Schecter, Squier, and Steinberger models
        26.5″ (673.2mmm) most 7 string models by Ibanez, Jackson & Schecter
        27-30″ (686 – 762mm) guitars in this range are called ‘baritone’ guitars. Also used by most 8 & 9 string guitars
        34″ (863.6mm) standard bass guitars
        """

        self.scale_ratio = 17.817
        self.guitars = {
            'Fender Jaguar, Fender Mustang': {'metric': 610, 'imperial': 24.0, 'frets': 22},
            'Paul Reed Smith Santana Signature series': {'metric': 622, 'imperial': 24.5, 'frets': 24},
            'Most Gibson and Epiphone models': {'metric': 628, 'imperial': 24.75, 'frets': 22},
            'Most PRS, Carvin, and Danelectric models': {'metric': 635, 'imperial': 25.0, 'frets': 22},
            'Most Fender, Ibanez, Jackson, Kramer, Schecter, Squier, and Steinberger models': {'metric': 648, 'imperial': 25.5, 'frets': 22},
            'Most 7 string models by Ibanez, Jackson & Schecter': {'metric': 673.2, 'imperial': 26.5, 'frets': 22},
            'Standard bass guitards': {'metric': 863.6, 'imperial': 34.0, 'frets': 22}
        }

        self.calculate()

    def calculate(self):

        for key in self.guitars:
            print('\n*** {name} ***'.format(name=key))
            print('Scale length: metric: {scale_m} mm imperial: {scale_i} inch'.format(scale_m=self.guitars[key]['metric'],
                                                                                       scale_i=self.guitars[key]['imperial']))
            print('Distance nut to fret:\n')
            scale_metric = self.guitars[key]['metric']
            scale_imperial = self.guitars[key]['imperial']
            distance_metric = 0
            distance_imperial = 0

            for fret in range(1, self.guitars[key]['frets'] + 1, 1):
                location_metric = scale_metric - distance_metric
                scaling_factor_metric = location_metric / 17.817
                distance_metric = distance_metric + scaling_factor_metric

                location_imperial = scale_imperial - distance_imperial
                scaling_factor_imperial = location_imperial / 17.817
                distance_imperial = distance_imperial + scaling_factor_imperial

                str_distance_metric = '{distance_metric:.{pre}f} mm'.format(distance_metric=distance_metric, pre=2)
                str_distance_imperial = '{distance_imperial:.{pre}f} inch'.format(distance_imperial=distance_imperial, pre=2)

                print('Fret: {fret: >2}\tmetric: {str_distance_metric: >9} imperial: {str_distance_imperial: >10}'.format(fret=fret,
                                                                                                                          str_distance_metric=str_distance_metric,
                                                                                                                          str_distance_imperial=str_distance_imperial))


if __name__ == "__main__":
    GuitarFretSpaces()
