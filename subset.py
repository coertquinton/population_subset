import itertools
import datetime
import time


class SubsetCalculator(object):

    def get_subset(self, my_list, target_number):

        for i in range(1, len(my_list)+1):
            total_tupple = itertools.combinations(my_list, i)
            subset_tupple = self.test_sublist(total_tupple, target_number, i)

            if (subset_tupple):
                return subset_tupple

        return None

    def test_sublist(self, total_tupple, sub_number, i):
        print("starting on tupple length %s at %s" % (i, str(datetime.datetime.now())))

        for sub_list in total_tupple:
            x = 0
            precise_list = []
            for number in sub_list:
                precise_list.append(number)
                x = x + number
                if x > sub_number:
                    break

                if x == sub_number:
                    return precise_list

        
        
calculator = SubsetCalculator()

my_list = [18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
total = sum(my_list)
print('Total of all numbers together is {}.'.format(total))
target_number = 101000000

subset = calculator.get_subset(my_list, target_number)
if subset:
    print('The subset which gives {} is {}.'.format(target_number, subset))
    print('The sum of the subset is {}'.format(sum(subset)))

else:
    print('No subset of {} gives {}.'.format(subset, target_number))


