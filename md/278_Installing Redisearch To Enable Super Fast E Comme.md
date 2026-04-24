> **Experimental**

ERPNext 的电子商务模块可选使用 RediSearch 来启用搜索功能，可通过 **电子商务设置** 进行配置。

安装并配置后，RediSearch 将用于驱动电子商务网站的搜索功能。这包括模糊词搜索、自动完成、结果排序和可自定义字段索引等功能。

### 前置条件

- Frappe Framework + ERPNext 环境

- Redis 6+

### 安装说明

```
$ git clone --recursive https://github.com/RediSearch/RediSearch.git
$ cd RediSearch
$ sudo make setup # 在 macOS 上移除 `sudo`
$ make build
  

```

> 请注意：最新版本的 RediSearch 需要 Redis 7.1+，而截至 2023 年 8 月 1 日，snap 仓库中的稳定版 Redis 为 7.0。因此，需要从源码编译 Redis 才能与 RediSearch 兼容。

同时请注意，ERPNext 需要 Redis 6+，因此使用 Redis 7.1+ 可能会导致问题。使用 Redis 7.1+ 时请谨慎。

按照上述说明成功完成后，`redisearch.so` 二进制文件将在 `RediSearch/build` 目录中生成。

将此二进制文件移动到 `/etc` 目录并重启 Frappe Server：

```
sudo mv build/redisearch.so /etc/
  

```

现在，打开位于 `config` 目录（bench 目录内）中的 `redis_cache.conf` 文件。在 `save ""` 行之前添加以下行，然后重启 bench server：

```
loadmodule /etc/redisearch.so
  

```

这将在启动时加载 redisearch 模块。可以通过在 `redis-cli -p 13000` 中运行以下命令来检查模块是否成功加载（假设端口为 frappe 配置中的默认端口 13000）：

```
> MODULE LIST
  

```

`search` 应该是列出的模块之一。

您也可以通过在 `redis-cli` 中运行以下命令来加载正在运行的 redis 实例上的模块：

```
> MODULE LOAD /etc/redisearch.so
  

```

> 我们将 `redisearch.so` 模块放置在 `/etc` 目录中，但可以放置在文件系统中的任何位置。我们使用此目录是因为将来 `loadmodule` 行将自动填充到配置文件中，并且它将假定二进制文件在 `/etc` 目录中。

> 更详细的说明可在[此处](https://github.com/RediSearch/redisearch-getting-started/blob/master/docs/002-install-redisearch.md)找到。

---
original_url: https://docs.frappe.io/erpnext/installing_redisearch_to_enable_super_fast_e_commerce_search
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---