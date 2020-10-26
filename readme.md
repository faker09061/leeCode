# leeCode算法

主要用来保存刷算法的题目

# 板子

## BFS

```c++
void bfs(起始点)
{
	将起始点放入队列中;
	标记起点访问;
	while(如果队列不为空)
	{
		访问队列首元素X;
		删除队首元素;
		for(X 所有相邻点)
		{
			if(该点未被访问过且合法)
			{
				将该点加入队列末尾; 
			}
		} 
	} 
	队列为空，广搜结束; 
}
```
这里得BFS主要是非递归得形式，也就是采用一个大队列得形式。

主要步骤：
- 加入初始点
- 开始循环
    - 取出队首元素
    - 判断需要加入得元素
    - 判断队列是否为空结束循环


基本得是上面，但是实际上，我们可能需要许多细节操作。必须打表，判断不必要得加入。


## DFS

dfs 可以使用递归和非递归得办法
非递归主要可以使用数据结构，栈。


```java
DFS（顶点） # 可以传入其他保存当前dfs路径的值，比如状态参数
{
　　处理当前顶点，记录为已访问
　　遍历与当前顶点相邻的所有未访问顶点
　　{
　　　　　　标记更改;
　　　　　　DFS( 下一子状态);
　　　　　　恢复更改;
　　}
}
```

## DP动态规划

步骤：
- 确定题目可以将问题得数量级之间通过子问题进行重构。也就是当前得答案可以由其之前得问题（更加小一个数量得问题）进行简单计算得到
- 然后初始化边界问题
- 然后开始递推（或者递归）

常用技巧，备忘录减小计算量。

```java
//DP问题 板子
//背包问题
//1,正向、逆向循环i
void dp()
{
    for(int i = 0; i < n; i ++)
    {
        for(int j = 0; j <= W; j ++)
        {
            if(j+w[i]<=W)
            {
                dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i]);//i逆向循环则dp[i][j] = max(dp[i+1][j],dp[i+1][j-w[i]]+v[i])
            }
            else
                dp[i+1][j] = dp[i][j];//i逆向循环则dp[i][j] = dp[i+1][j]
        }
    }
}
//2
void dp()
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j <= W; j ++)
        {
            dp[i+1][j] = max(dp[i][j],dp[i+1][j]);
            if(j+w[i] <= W)
                dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]],dp[i][j]+v[i]);
        }
    }
}
```
