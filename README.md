Shadows council 
https://drive.google.com/drive/folders/1bTxc9SpilQzu_AiqeTrl72ISIFcaY5Fr

YOUR 10-MINUTE MEMORY SHEET

If you're extremely short on time, memorize this:

### Bubble
```
for(i=0;i<n-1;i++)
 for(j=0;j<n-i-1;j++)
  if(a[j]>a[j+1])
   swap(a[j],a[j+1]);
```

### Insertion
```key=a[i];
j=i-1;

while(j>=0 && a[j]>key)
{
    a[j+1]=a[j];
    j--;
}

a[j+1]=key;
```
### Counting
```count[a[i]]++;

Then:

for(i=0;i<range;i++)
 while(count[i]--)
    cout << i;
```
### Min/Max
```min=max=a[0];

if(a[i]<min) min=a[i];
if(a[i]>max) max=a[i];
```
### Heap
```left=2*i+1;
right=2*i+2;
```
### Build heap:
```
for(i=n/2-1;i>=0;i--)
    heapify(a,n,i);
```
### Merge
```Divide → Sort → Merge```

### Quick
```Pivot → Partition → Recursion```

### Binary Search
```mid=(low+high)/2;
equal → found
smaller → left
larger → right
```

### Matrix
```C[i][j] += A[i][k] * B[k][j];```

### Strassen
```
7 M values + 4 C formulas.
```


7 M values + 4 C formulas.
