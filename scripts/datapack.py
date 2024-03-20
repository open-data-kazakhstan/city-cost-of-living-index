from datapackage import Package

package = Package()

package.infer(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost.csv')
package.infer(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost_piv.csv')
package.infer(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\spend.csv')
package.infer(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\spend_piv.csv')

package.commit()
package.save(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\datapackage.json')