>> a =[-1.2, 3.1, 4.7, 1.9]

a =

   -1.2000    3.1000    4.7000    1.9000

>> a =[-1.2, 3.1, 4.7, 1.9]

a =

   -1.2000    3.1000    4.7000    1.9000

>> a =[-1.2, 3.1, 4.7, 1.9]

a =

   -1.2000    3.1000    4.7000    1.9000

>> a =[-1.2; 3.1; 4.7; 1.9]

a =

   -1.2000
    3.1000
    4.7000
    1.9000

>> a(1)

ans =

   -1.2000

>> length(a)

ans =

     4

>> n=length(a)

n =

     4

>> m=length(a);
>> n+m

ans =

     8

>> a*n

ans =

   -4.8000
   12.4000
   18.8000
    7.6000

>> b=1:10

b =

  Columns 1 through 9

     1     2     3     4     5     6     7     8     9

  Column 10

    10

>> c=10:-1:1

c =

  Columns 1 through 9

    10     9     8     7     6     5     4     3     2

  Column 10

     1

>> d=2:0.2:3

d =

  Columns 1 through 5

    2.0000    2.2000    2.4000    2.6000    2.8000

  Column 6

    3.0000

>> f=linspace(1,2)

f =

  Columns 1 through 5

    1.0000    1.0101    1.0202    1.0303    1.0404

  Columns 6 through 10

    1.0505    1.0606    1.0707    1.0808    1.0909

  Columns 11 through 15

    1.1010    1.1111    1.1212    1.1313    1.1414

  Columns 16 through 20

    1.1515    1.1616    1.1717    1.1818    1.1919

  Columns 21 through 25

    1.2020    1.2121    1.2222    1.2323    1.2424

  Columns 26 through 30

    1.2525    1.2626    1.2727    1.2828    1.2929

  Columns 31 through 35

    1.3030    1.3131    1.3232    1.3333    1.3434

  Columns 36 through 40

    1.3535    1.3636    1.3737    1.3838    1.3939

  Columns 41 through 45

    1.4040    1.4141    1.4242    1.4343    1.4444

  Columns 46 through 50

    1.4545    1.4646    1.4747    1.4848    1.4949

  Columns 51 through 55

    1.5051    1.5152    1.5253    1.5354    1.5455

  Columns 56 through 60

    1.5556    1.5657    1.5758    1.5859    1.5960

  Columns 61 through 65

    1.6061    1.6162    1.6263    1.6364    1.6465

  Columns 66 through 70

    1.6566    1.6667    1.6768    1.6869    1.6970

  Columns 71 through 75

    1.7071    1.7172    1.7273    1.7374    1.7475

  Columns 76 through 80

    1.7576    1.7677    1.7778    1.7879    1.7980

  Columns 81 through 85

    1.8081    1.8182    1.8283    1.8384    1.8485

  Columns 86 through 90

    1.8586    1.8687    1.8788    1.8889    1.8990

  Columns 91 through 95

    1.9091    1.9192    1.9293    1.9394    1.9495

  Columns 96 through 100

    1.9596    1.9697    1.9798    1.9899    2.0000

>> e=linspace(1,2,6)

e =

  Columns 1 through 5

    1.0000    1.2000    1.4000    1.6000    1.8000

  Column 6

    2.0000

>> m=[-1;3;5;66]

m =

    -1
     3
     5
    66

>> m=m'

m =

    -1     3     5    66

>> m=m''

m =

    -1     3     5    66

>> m=m'

m =

    -1
     3
     5
    66

>> m(2)

ans =

     3

>> size(m)

ans =

     4     1

>> size(m')

ans =

     1     4

>> m

m =

    -1
     3
     5
    66

>> [b c]

ans =

  Columns 1 through 9

     1     2     3     4     5     6     7     8     9

  Columns 10 through 18

    10    10     9     8     7     6     5     4     3

  Columns 19 through 20

     2     1

>> [-1 0 b]

ans =

  Columns 1 through 9

    -1     0     1     2     3     4     5     6     7

  Columns 10 through 12

     8     9    10

>> b

b =

  Columns 1 through 9

     1     2     3     4     5     6     7     8     9

  Column 10

    10

>> b(2:4)

ans =

     2     3     4

>> b([1 3 7])

ans =

     1     3     7

>> a=0:30

a =

  Columns 1 through 9

     0     1     2     3     4     5     6     7     8

  Columns 10 through 18

     9    10    11    12    13    14    15    16    17

  Columns 19 through 27

    18    19    20    21    22    23    24    25    26

  Columns 28 through 31

    27    28    29    30

>> a=0:1:30

a =

  Columns 1 through 9

     0     1     2     3     4     5     6     7     8

  Columns 10 through 18

     9    10    11    12    13    14    15    16    17

  Columns 19 through 27

    18    19    20    21    22    23    24    25    26

  Columns 28 through 31

    27    28    29    30

>> 
>> b=2:2:100

b =

  Columns 1 through 9

     2     4     6     8    10    12    14    16    18

  Columns 10 through 18

    20    22    24    26    28    30    32    34    36

  Columns 19 through 27

    38    40    42    44    46    48    50    52    54

  Columns 28 through 36

    56    58    60    62    64    66    68    70    72

  Columns 37 through 45

    74    76    78    80    82    84    86    88    90

  Columns 46 through 50

    92    94    96    98   100

>> c=2:-0.1:0

c =

  Columns 1 through 5

    2.0000    1.9000    1.8000    1.7000    1.6000

  Columns 6 through 10

    1.5000    1.4000    1.3000    1.2000    1.1000

  Columns 11 through 15

    1.0000    0.9000    0.8000    0.7000    0.6000

  Columns 16 through 20

    0.5000    0.4000    0.3000    0.2000    0.1000

  Column 21

         0

>> d=0:3:30 -100 30:-3:0
 d=0:3:30 -100 30:-3:0
               ↑
Invalid expression. Check for missing multiplication
operator, missing or unbalanced delimiters, or other
syntax error. To construct matrices, use brackets
instead of parentheses.
 
>> d=[0:3:30 -100 30:-3:0]

d =

  Columns 1 through 9

     0     3     6     9    12    15    18    21    24

  Columns 10 through 18

    27    30  -100    30    27    24    21    18    15

  Columns 19 through 23

    12     9     6     3     0

>> a=2:20

a =

  Columns 1 through 9

     2     3     4     5     6     7     8     9    10

  Columns 10 through 18

    11    12    13    14    15    16    17    18    19

  Column 19

    20

>> e=1./a

e =

  Columns 1 through 5

    0.5000    0.3333    0.2500    0.2000    0.1667

  Columns 6 through 10

    0.1429    0.1250    0.1111    0.1000    0.0909

  Columns 11 through 15

    0.0833    0.0769    0.0714    0.0667    0.0625

  Columns 16 through 19

    0.0588    0.0556    0.0526    0.0500

>> format rat
>> e

e =

  Columns 1 through 4

       1/2            1/3            1/4            1/5     

  Columns 5 through 8

       1/6            1/7            1/8            1/9     

  Columns 9 through 12

       1/10           1/11           1/12           1/13    

  Columns 13 through 16

       1/14           1/15           1/16           1/17    

  Columns 17 through 19

       1/18           1/19           1/20    

>> f=[1:19]./[2:20]

f =

  Columns 1 through 4

       1/2            2/3            3/4            4/5     

  Columns 5 through 8

       5/6            6/7            7/8            8/9     

  Columns 9 through 12

       9/10          10/11          11/12          12/13    

  Columns 13 through 16

      13/14          14/15          15/16          16/17    

  Columns 17 through 19

      17/18          18/19          19/20    

>> x=linspace(1,100)

x =

  Columns 1 through 4

       1              2              3              4       

  Columns 5 through 8

       5              6              7              8       

  Columns 9 through 12

       9             10             11             12       

  Columns 13 through 16

      13             14             15             16       

  Columns 17 through 20

      17             18             19             20       

  Columns 21 through 24

      21             22             23             24       

  Columns 25 through 28

      25             26             27             28       

  Columns 29 through 32

      29             30             31             32       

  Columns 33 through 36

      33             34             35             36       

  Columns 37 through 40

      37             38             39             40       

  Columns 41 through 44

      41             42             43             44       

  Columns 45 through 48

      45             46             47             48       

  Columns 49 through 52

      49             50             51             52       

  Columns 53 through 56

      53             54             55             56       

  Columns 57 through 60

      57             58             59             60       

  Columns 61 through 64

      61             62             63             64       

  Columns 65 through 68

      65             66             67             68       

  Columns 69 through 72

      69             70             71             72       

  Columns 73 through 76

      73             74             75             76       

  Columns 77 through 80

      77             78             79             80       

  Columns 81 through 84

      81             82             83             84       

  Columns 85 through 88

      85             86             87             88       

  Columns 89 through 92

      89             90             91             92       

  Columns 93 through 96

      93             94             95             96       

  Columns 97 through 100

      97             98             99            100       

>> help rand
 rand Uniformly distributed pseudorandom numbers.
    R = rand(N) returns an N-by-N matrix containing pseudorandom values drawn
    from the standard uniform distribution on the open interval(0,1).  rand(M,N)
    or rand([M,N]) returns an M-by-N matrix.  rand(M,N,P,...) or
    rand([M,N,P,...]) returns an M-by-N-by-P-by-... array.  rand returns a
    scalar.  rand(SIZE(A)) returns an array the same size as A.
 
    Note: The size inputs M, N, P, ... should be nonnegative integers.
    Negative integers are treated as 0.
 
    R = rand(..., CLASSNAME) returns an array of uniform values of the 
    specified class. CLASSNAME can be 'double' or 'single'.
 
    R = rand(..., 'like', Y) returns an array of uniform values of the 
    same class as Y.
 
    The sequence of numbers produced by rand is determined by the settings of
    the uniform random number generator that underlies rand, RANDI, and RANDN.
    Control that shared random number generator using RNG.
 
    Examples:
 
       Example 1: Generate values from the uniform distribution on the
       interval (a, b).
          r = a + (b-a).*rand(100,1);
 
       Example 2: Use the RANDI function, instead of rand, to generate
       integer values from the uniform distribution on the set 1:100.
          r = randi(100,1,5);
 
       Example 3: Reset the random number generator used by rand, RANDI, and
       RANDN to its default startup settings, so that rand produces the same
       random numbers as if you restarted MATLAB.
          rng('default')
          rand(1,5)
 
       Example 4: Save the settings for the random number generator used by
       rand, RANDI, and RANDN, generate 5 values from rand, restore the
       settings, and repeat those values.
          s = rng
          u1 = rand(1,5)
          rng(s);
          u2 = rand(1,5) % contains exactly the same values as u1
 
       Example 5: Reinitialize the random number generator used by rand,
       RANDI, and RANDN with a seed based on the current time.  rand will
       return different values each time you do this.  NOTE: It is usually
       not necessary to do this more than once per MATLAB session.
          rng('shuffle');
          rand(1,5)
 
    See Replace Discouraged Syntaxes of rand and randn to use RNG to replace
    rand with the 'seed', 'state', or 'twister' inputs.
 
    See also randi, randn, rng, RandStream, RandStream/rand,
             sprand, sprandn, randperm.

    Documentation for rand
    Other functions named rand

>> flip(x)

ans =

  Columns 1 through 4

     100             99             98             97       

  Columns 5 through 8

      96             95             94             93       

  Columns 9 through 12

      92             91             90             89       

  Columns 13 through 16

      88             87             86             85       

  Columns 17 through 20

      84             83             82             81       

  Columns 21 through 24

      80             79             78             77       

  Columns 25 through 28

      76             75             74             73       

  Columns 29 through 32

      72             71             70             69       

  Columns 33 through 36

      68             67             66             65       

  Columns 37 through 40

      64             63             62             61       

  Columns 41 through 44

      60             59             58             57       

  Columns 45 through 48

      56             55             54             53       

  Columns 49 through 52

      52             51             50             49       

  Columns 53 through 56

      48             47             46             45       

  Columns 57 through 60

      44             43             42             41       

  Columns 61 through 64

      40             39             38             37       

  Columns 65 through 68

      36             35             34             33       

  Columns 69 through 72

      32             31             30             29       

  Columns 73 through 76

      28             27             26             25       

  Columns 77 through 80

      24             23             22             21       

  Columns 81 through 84

      20             19             18             17       

  Columns 85 through 88

      16             15             14             13       

  Columns 89 through 92

      12             11             10              9       

  Columns 93 through 96

       8              7              6              5       

  Columns 97 through 100

       4              3              2              1       

>> x(1:5)

ans =

  Columns 1 through 4

       1              2              3              4       

  Column 5

       5       

>> x(4)=[]

x =

  Columns 1 through 4

       1              2              3              5       

  Columns 5 through 8

       6              7              8              9       

  Columns 9 through 12

      10             11             12             13       

  Columns 13 through 16

      14             15             16             17       

  Columns 17 through 20

      18             19             20             21       

  Columns 21 through 24

      22             23             24             25       

  Columns 25 through 28

      26             27             28             29       

  Columns 29 through 32

      30             31             32             33       

  Columns 33 through 36

      34             35             36             37       

  Columns 37 through 40

      38             39             40             41       

  Columns 41 through 44

      42             43             44             45       

  Columns 45 through 48

      46             47             48             49       

  Columns 49 through 52

      50             51             52             53       

  Columns 53 through 56

      54             55             56             57       

  Columns 57 through 60

      58             59             60             61       

  Columns 61 through 64

      62             63             64             65       

  Columns 65 through 68

      66             67             68             69       

  Columns 69 through 72

      70             71             72             73       

  Columns 73 through 76

      74             75             76             77       

  Columns 77 through 80

      78             79             80             81       

  Columns 81 through 84

      82             83             84             85       

  Columns 85 through 88

      86             87             88             89       

  Columns 89 through 92

      90             91             92             93       

  Columns 93 through 96

      94             95             96             97       

  Columns 97 through 99

      98             99            100       

>> x([5 72 93])=[]

x =

  Columns 1 through 4

       1              2              3              5       

  Columns 5 through 8

       7              8              9             10       

  Columns 9 through 12

      11             12             13             14       

  Columns 13 through 16

      15             16             17             18       

  Columns 17 through 20

      19             20             21             22       

  Columns 21 through 24

      23             24             25             26       

  Columns 25 through 28

      27             28             29             30       

  Columns 29 through 32

      31             32             33             34       

  Columns 33 through 36

      35             36             37             38       

  Columns 37 through 40

      39             40             41             42       

  Columns 41 through 44

      43             44             45             46       

  Columns 45 through 48

      47             48             49             50       

  Columns 49 through 52

      51             52             53             54       

  Columns 53 through 56

      55             56             57             58       

  Columns 57 through 60

      59             60             61             62       

  Columns 61 through 64

      63             64             65             66       

  Columns 65 through 68

      67             68             69             70       

  Columns 69 through 72

      71             72             74             75       

  Columns 73 through 76

      76             77             78             79       

  Columns 77 through 80

      80             81             82             83       

  Columns 81 through 84

      84             85             86             87       

  Columns 85 through 88

      88             89             90             91       

  Columns 89 through 92

      92             93             95             96       

  Columns 93 through 96

      97             98             99            100       

>> x([1:2:end)=[]
 x([1:2:end)=[]
           ↑
Invalid expression. When calling a function or indexing
a variable, use parentheses. Otherwise, check for
mismatched delimiters.
 
>> x([1:2:end)]=[]
 x([1:2:end)]=[]
           ↑
Invalid expression. When calling a function or indexing
a variable, use parentheses. Otherwise, check for
mismatched delimiters.
 
Did you mean:
>> x([1:2:end])=[]

x =

  Columns 1 through 4

       2              5              8             10       

  Columns 5 through 8

      12             14             16             18       

  Columns 9 through 12

      20             22             24             26       

  Columns 13 through 16

      28             30             32             34       

  Columns 17 through 20

      36             38             40             42       

  Columns 21 through 24

      44             46             48             50       

  Columns 25 through 28

      52             54             56             58       

  Columns 29 through 32

      60             62             64             66       

  Columns 33 through 36

      68             70             72             75       

  Columns 37 through 40

      77             79             81             83       

  Columns 41 through 44

      85             87             89             91       

  Columns 45 through 48

      93             96             98            100       

>> x(2 5 17 81)
 x(2 5 17 81)
     ↑
Invalid expression. Check for missing multiplication
operator, missing or unbalanced delimiters, or other
syntax error. To construct matrices, use brackets
instead of parentheses.
 
>> x([2 5 17 81])
Index exceeds the number of array elements. Index must
not exceed 48.
 
>> x=([2 5 17 81])

x =

       2              5             17             81       

>> x=[1:10]

x =

  Columns 1 through 4

       1              2              3              4       

  Columns 5 through 8

       5              6              7              8       

  Columns 9 through 10

       9             10       

>> y1=x+2

y1 =

  Columns 1 through 4

       3              4              5              6       

  Columns 5 through 8

       7              8              9             10       

  Columns 9 through 10

      11             12       

>> y2=x^2
Error using  ^  (line 52)
Incorrect dimensions for raising a matrix to a power.
Check that the matrix is square and the power is a
scalar. To perform elementwise matrix powers, use '.^'.
 
>> y2=x.^2

y2 =

  Columns 1 through 4

       1              4              9             16       

  Columns 5 through 8

      25             36             49             64       

  Columns 9 through 10

      81            100       

>> 
>> y3=1./x

y3 =

  Columns 1 through 4

       1              1/2            1/3            1/4     

  Columns 5 through 8

       1/5            1/6            1/7            1/8     

  Columns 9 through 10

       1/9            1/10    

>> y4=sin(x.^3-1)

y4 =

  Columns 1 through 4

       0           1561/2376      2611/3424      1093/6531  

  Columns 5 through 8

   -1616/1623      1836/1873      1865/4439      1514/1717  

  Columns 9 through 10

    -793/1056      -269/10166 

>> format short
>> y4=sin(x.^3-1)

y4 =

  Columns 1 through 5

         0    0.6570    0.7626    0.1674   -0.9957

  Columns 6 through 10

    0.9802    0.4201    0.8818   -0.7509   -0.0265

>> y5=x-[1:length(x)]

y5 =

  Columns 1 through 9

     0     0     0     0     0     0     0     0     0

  Column 10

     0

>> y5=x-[1:length(x)]

y5 =

  Columns 1 through 9

     0     0     0     0     0     0     0     0     0

  Column 10

     0

>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> A=[1 2 3;4 5 6;7 8 9]

A =

     1     2     3
     4     5     6
     7     8     9

>> E=eye(3,4)

E =

     1     0     0     0
     0     1     0     0
     0     0     1     0

>> E=eye(5)

E =

     1     0     0     0     0
     0     1     0     0     0
     0     0     1     0     0
     0     0     0     1     0
     0     0     0     0     1

>> x=[-1 4 0]

x =

    -1     4     0

>> y=[3 -2 5]

y =

     3    -2     5

>> A=[-3 1 -4;6 2 -5]

A =

    -3     1    -4
     6     2    -5

>> z=[x;y]

z =

    -1     4     0
     3    -2     5

>> z=[x,y]

z =

    -1     4     0     3    -2     5

>> z=[x',y']

z =

    -1     3
     4    -2
     0     5

>> z=[x';y']

z =

    -1
     4
     0
     3
    -2
     5

>> z=[A;x]

z =

    -3     1    -4
     6     2    -5
    -1     4     0

>> z=[A,x]
Error using horzcat
Dimensions of arrays being concatenated are not
consistent.
 
>> z = [x; A; y]

z =

    -1     4     0
    -3     1    -4
     6     2    -5
     3    -2     5

>> z = [A';x]
Error using vertcat
Dimensions of arrays being concatenated are not
consistent.
 
>> z = [A',x]
Error using horzcat
Dimensions of arrays being concatenated are not
consistent.
 
>> z=[A';x]
Error using vertcat
Dimensions of arrays being concatenated are not
consistent.
 
>> z=[A',x']

z =

    -3     6    -1
     1     2     4
    -4    -5     0

>> x+y

ans =

     2     2     5

>> x+y'

ans =

     2     7     3
    -3     2    -2
     4     9     5

>> A+y

ans =

     0    -1     1
     9     0     0

>> A+2

ans =

    -1     3    -2
     8     4    -3

>> x./y

ans =

   -0.3333   -2.0000         0

>> A^2
Error using  ^  (line 52)
Incorrect dimensions for raising a matrix to a power.
Check that the matrix is square and the power is a
scalar. To perform elementwise matrix powers, use '.^'.
 
>> A.^2

ans =

     9     1    16
    36     4    25

>> A=ones(2)

A =

     1     1
     1     1

>> A^2

ans =

     2     2
     2     2

>> A.^2

ans =

     1     1
     1     1

>> A=(1 2 3 4;5 6 7 8;9 10 11 12)
 A=(1 2 3 4;5 6 7 8;9 10 11 12)
      ↑
Invalid expression. Check for missing multiplication
operator, missing or unbalanced delimiters, or other
syntax error. To construct matrices, use brackets
instead of parentheses.
 
>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(1,:)=[]

A =

     5     6     7     8
     9    10    11    12

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(:,[2 4])=[]

A =

     1     3
     5     7
     9    11

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A([3,4])=[]

A =

  Columns 1 through 9

     1     5     6    10     3     7    11     4     8

  Column 10

    12

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> n=size(A)

n =

     3     4

>> A(:,n(2))=[]

A =

     1     2     3
     5     6     7
     9    10    11

>> A(n(1),:)=[]

A =

     1     2     3
     5     6     7

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> (A,A)
 (A,A)
   ↑
Invalid expression. When calling a function or indexing
a variable, use parentheses. Otherwise, check for
mismatched delimiters.
 
>> [A,A]

ans =

     1     2     3     4     1     2     3     4
     5     6     7     8     5     6     7     8
     9    10    11    12     9    10    11    12

>> A'

ans =

     1     5     9
     2     6    10
     3     7    11
     4     8    12

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(:,[2,4])=A(:,[4,1])

A =

     1     4     3     1
     5     8     7     5
     9    12    11     9

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(:,[2,4])=A(:,[4,2])

A =

     1     4     3     2
     5     8     7     6
     9    12    11    10

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A.^2

ans =

     1     4     9    16
    25    36    49    64
    81   100   121   144

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A+3

ans =

     4     5     6     7
     8     9    10    11
    12    13    14    15

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A.^0.5

ans =

    1.0000    1.4142    1.7321    2.0000
    2.2361    2.4495    2.6458    2.8284
    3.0000    3.1623    3.3166    3.4641

>> A=sin(A)

A =

    0.8415    0.9093    0.1411   -0.7568
   -0.9589   -0.2794    0.6570    0.9894
    0.4121   -0.5440   -1.0000   -0.5366

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(1,2)=-2

A =

     1    -2     3     4
     5     6     7     8
     9    10    11    12

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(1,:)=[-1 0 -2 3]

A =

    -1     0    -2     3
     5     6     7     8
     9    10    11    12

>> A=[1 2 3 4;5 6 7 8;9 10 11 12]

A =

     1     2     3     4
     5     6     7     8
     9    10    11    12

>> A(2,:)=[-1 0 -2 3]

A =

     1     2     3     4
    -1     0    -2     3
     9    10    11    12

>> A=[1:8;20:-2:6;2.^[1:8]]

A =

     1     2     3     4     5     6     7     8
    20    18    16    14    12    10     8     6
     2     4     8    16    32    64   128   256

>> sum(A)

ans =

    23    24    27    34    49    80   143   270

>> sum(A,2)

ans =

    36
   104
   510

>> sum(A,1)

ans =

    23    24    27    34    49    80   143   270

>> reshape(A,6,4)

ans =

     1     3     5     7
    20    16    12     8
     2     8    32   128
     2     4     6     8
    18    14    10     6
     4    16    64   256

>> max(A)

ans =

    20    18    16    16    32    64   128   256

>> max(A,[],2)

ans =

     8
    20
   256

>> flipud(A)

ans =

     2     4     8    16    32    64   128   256
    20    18    16    14    12    10     8     6
     1     2     3     4     5     6     7     8

>> fliplr(A)

ans =

     8     7     6     5     4     3     2     1
     6     8    10    12    14    16    18    20
   256   128    64    32    16     8     4     2

>> a=[1 1 1]

a =

     1     1     1

>> diag(a)

ans =

     1     0     0
     0     1     0
     0     0     1

>> diag(a,2)

ans =

     0     0     1     0     0
     0     0     0     1     0
     0     0     0     0     1
     0     0     0     0     0
     0     0     0     0     0

>> A=[1:8;20:-2:6;2.^[1:8]]

A =

     1     2     3     4     5     6     7     8
    20    18    16    14    12    10     8     6
     2     4     8    16    32    64   128   256

>> diag(A)

ans =

     1
    18
     8

>> diag(A,3)

ans =

     4
    12
    64

>> tril(A)

ans =

     1     0     0     0     0     0     0     0
    20    18     0     0     0     0     0     0
     2     4     8     0     0     0     0     0

>> triu(A)

ans =

     1     2     3     4     5     6     7     8
     0    18    16    14    12    10     8     6
     0     0     8    16    32    64   128   256

>> y=elsofuggvenyem(2)

y =

     7

>> y=elsofuggvenyem([2,2,3])

y =

     7     7    14

>> [output1,output2]=elsofuggvenyem(2)
Error using elsofuggvenyem
Too many output arguments.
 
>> [output1,output2]=elsofuggvenyem(2)
Error using elsofuggvenyem
Too many output arguments.
 
>> [output1,output2]=elsofuggvenyem(2)

output1 =

     7


output2 =

     4

>> 
