      program problem1
      integer sum, counter, MAX
      parameter (MAX = 1000)

C     Find the sum of all the multiples of 3 or 5 below 1000

      sum = 0

C     Sum all multiples of 3
      do 10 counter = 3, MAX-1, 3
         sum = sum + counter
 10   continue

C     Sum all multiples of 5
      do 20 counter = 5, MAX-1, 5
         sum = sum + counter
 20   continue

C     Subtract multiples of 15 to avoid double counting
      do 30 counter = 15, MAX-1, 15
         sum = sum - counter
 30   continue

      write (*, *) 'The sum is ', sum

      stop
      end
