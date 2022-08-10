https://didiboy0702.gitbook.io/wukongdaily/wan-ke-yun-ji-qiao/ytdlp-8k-xia-zai-shen-qi-shi-yong-jian-jie

YT-DLP

发布版本 派皮 捐 矩阵 不和谐 支持的站点 执照：无执照 CI 状态 提交 最后提交

yt-dlp 是基于现在不活动的youtube-dlc的youtube-dl分支。该项目的主要重点是添加新功能和补丁，同时与原始项目保持同步

新的功能
默认行为的差异
安装
更新
发布文件
依赖项
编译
用法和选项
常规选项
网络选项
地理限制
视频选择
下载选项
文件系统选项
缩略图选项
Internet 快捷方式选项
详细程度和模拟选项
解决方法
视频格式选项
字幕选项
身份验证选项
后处理选项
赞助商区块选项
提取器选项
配置
使用 .netrc 文件进行身份验证
输出模板
输出模板和 Windows 批处理文件
输出模板示例
格式选择
过滤格式
排序格式
格式选择示例
修改元数据
修改元数据示例
提取器参数
插件
嵌入 YT-DLP
嵌入示例
不推荐使用的选项
贡献
打开一个问题
开发人员说明
更多的
新的功能
与youtube-dl v2021.12.17+ commit/a03b977和youtube-dlc v2020.11.11-3+ commit/f9401f2 合并：除了最新的youtube-dl之外，您还可以获得youtube-dlc的所有功能和补丁

SponsorBlock 集成：您可以使用SponsorBlock API标记/删除 youtube 视频中的赞助商部分

格式排序：默认格式排序选项已更改，因此现在首选更高的分辨率和更好的编解码器，而不是简单地使用更大的比特率。此外，您现在可以使用 指定排序顺序-S。与简单地使用--format（示例）

与animelover1984/youtube-dl 合并：您可以从animalover1984/youtube-dl获得大部分功能和改进，包括、、、、--write-comments在mp4/ogg/opus 中嵌入缩略图、播放列表信息json 等。请注意，NicoNico 直播不可用。详见#31。BiliBiliSearchBilibiliChannel

YouTube 改进：

支持剪辑、故事 ( ytstories:<channel UCID>)、搜索（包括过滤器）*、YouTube 音乐搜索、频道特定搜索、搜索前缀 ( ytsearch:、ytsearchdate:) *、混音、YouTube 音乐专辑/频道（自上传音乐除外）和供稿（:ytfav、:ytwatchlater、:ytsubs, :ythistory, :ytrec, :ytnotif)
修复了基于 n-sig 的节流 *
支持一些（但不是全部）没有 cookie 的有年龄限制的内容
--live-from-start使用（实验性）从一开始就下载直播
255kbps提供高级 cookie 时从 YouTube Music 中提取音频（如果有）
自动重定向频道的主页 URL/video以保留旧行为
来自浏览器的Cookie：可以使用所有主要的网络浏览器自动提取 Cookie--cookies-from-browser BROWSER[+KEYRING][:PROFILE]

下载时间范围：可以使用时间戳或章节部分下载视频--download-sections

按章节分割视频：可以使用基于章节将视频分割成多个文件--split-chapters

多线程片段下载：并行下载 m3u8/mpd 视频的多个片段。使用--concurrent-fragments( -N) 选项设置使用的线程数

带有 HLS/DASH 的 Aria2c：您可以aria2c用作 DASH(mpd) 和 HLS(m3u8) 格式的外部下载器

新的和固定的提取器：添加了许多新的提取器，并且修复了许多现有的提取器。查看更新日志或支持站点列表

新的 MSO：Philo、Spectrum、SlingTV、Cablevision、RCN 等。

从清单中提取字幕：可以从流媒体清单中提取字幕。详情见commit /be6202f

多路径和输出模板：您可以为不同类型的文件提供不同的输出模板和下载路径。--paths您还可以使用( -P)设置下载中间文件的临时路径

可移植配置：配置文件从主目录和根目录自动加载。有关详细信息，请参阅配置

输出模板改进：输出模板现在可以具有日期时间格式、数字偏移量、对象遍历等。有关详细信息，请参阅输出模板。更高级的操作也可以在和的帮助下--parse-metadata完成--replace-in-metadata

其他新选项：添加了许多新选项，例如--alias, --print, --concat-playlist, --wait-for-video, --retry-sleep, --sleep-requests, --convert-thumbnails, --force-download-archive,--force-overwrites等--break-on-reject

改进：正则表达式和--format/中的其他运算符--match-filter，多个--postprocessor-args和--downloader-args，更快的存档检查，更多格式选择选项，合并多视频/音频，多个--config-locations，--exec在不同阶段等

插件：提取器和后处理器可以从外部文件加载。详情见插件_

Self-updater：可以使用更新版本yt-dlp -U

查看更改日志或提交以获取完整的更改列表

标有*的功能已向后移植到 youtube-dl

默认行为的差异
yt-dlp 的一些默认选项与 youtube-dl 和 youtube-dlc 不同：

选项--auto-number( -A)、--title( -t) 和--literal( -l) 不再起作用。有关详细信息，请参阅已删除的选项
avconv不支持作为替代ffmpeg
yt-dlp 将配置文件存储在与 youtube-dl 略有不同的位置。有关正确位置的列表，请参阅配置
默认输出模板是%(title)s [%(id)s].%(ext)s. 这种变化没有真正的原因。这在 yt-dlp 公开之前已更改，现在没有计划将其更改回%(title)s-%(id)s.%(ext)s. 相反，您可以使用--compat-options filename
默认格式排序与 youtube-dl 不同，它更喜欢更高的分辨率和更好的编解码器，而不是更高的比特率。您可以使用该--format-sort选项将其更改为您喜欢的任何顺序，或--compat-options format-sort使用 youtube-dl 的排序顺序
默认格式选择器是bv*+ba/b. 这意味着，如果找到比最佳纯视频格式更好的组合视频+音频格式，则首选前者。使用-f bv+ba/b或--compat-options format-spec恢复它
与 youtube-dlc 不同，yt-dlp 默认不允许将多个音频/视频流合并到一个文件中（因为这与使用 冲突-f bv*+ba）。如果需要，必须使用--audio-multistreams和启用此功能--video-multistreams。您也可以使用--compat-options multistreams同时启用
--no-abort-on-error默认启用。改为使用--abort-on-error或中止错误--compat-options abort-on-error
在编写缩略图、描述或 infojson 等元数据文件时，也会为播放列表编写相同的信息（如果可用）。使用--no-write-playlist-metafiles或--compat-options no-playlist-metafiles不写这些文件
--add-metadata与 .一起使用时，除了写入元数据外，还附加到infojson文件。使用或恢复它mkv--write-info-json--no-embed-info-json--compat-options no-attach-info-json
--add-metadata与 youtube-dl 相比，一些元数据在使用时被嵌入到不同的字段中。最值得注意comment的是，字段包含webpage_url并且synopsis包含description. 您可以根据自己的喜好修改它或使用它来--parse-metadata--compat-options embed-metadata恢复它
playlist_index--playlist-reverse与和等选项一起使用时表现不同--playlist-items。有关详细信息，请参阅#302。--compat-options playlist-index如果你想保持早期的行为，你可以使用
的输出-F以新格式列出。用于--compat-options list-formats还原此
实时聊天（如果可用）被视为字幕。用于--sub-langs all,-live_chat下载除实时聊天之外的所有字幕。您还可以--compat-options no-live-chat用来阻止任何实时聊天/弹幕下载
Youtube 频道 URL 会自动重定向到/video. 将 a 添加/featured到 URL 以仅下载主页中的视频。如果频道没有视频标签，我们会尝试下载等效的UU播放列表。对于所有其他选项卡，如果频道未显示请求的选项卡，则会引发错误。此外，/live如果没有实时视频而不是静默下载整个频道，则 URL 会引发错误。您可以使用--compat-options no-youtube-channel-redirect来还原所有这些重定向
youtube 播放列表中也列出了不可用的视频。用于--compat-options no-youtube-unavailable-videos删除此
如果ffmpeg用作下载器，则格式的下载和合并尽可能在一个步骤中进行。用于--compat-options no-direct-merge还原此
如果可能的话，嵌入缩略图mp4是用诱变剂完成的。使用--compat-options embed-thumbnail-atomicparsley来强制使用 AtomicParsley
默认情况下，一些私有字段（例如文件名）会从 infojson 中删除。使用--no-clean-infojson或--compat-options no-clean-infojson恢复它
当--embed-subs和--write-subs一起使用时，字幕会写入磁盘并嵌入到媒体文件中。您可以使用仅--embed-subs嵌入 subs 并自动删除单独的文件。有关更多信息，请参见#630（评论）。--compat-options no-keep-subs可以用来恢复这个
certifi将用于 SSL 根证书（如果已安装）。如果您想使用系统证书（例如自签名），请使用--compat-options no-certifi
youtube-dl 尝试从文件名中删除一些多余的标点符号。虽然这有时会有所帮助，但通常是不可取的。因此 yt-dlp 尝试使文件名中的字段尽可能接近其原始值。您可以--compat-options filename-sanitization用来恢复 youtube-dl 的行为
为了便于使用，提供了更多兼容选项：

--compat-options all：使用所有兼容选项（请勿使用）
--compat-options youtube-dl： 如同--compat-options all,-multistreams
--compat-options youtube-dlc： 如同--compat-options all,-no-live-chat,-no-youtube-channel-redirect
安装
您可以使用以下方法之一安装 yt-dlp：

使用发布二进制文件
您可以简单地为您的操作系统下载正确的二进制文件

视窗 Linux 苹果系统 源压缩包 其他变体 所有版本

注意：手册页、shell 完成文件等可在源 tarball中找到

在类 UNIX 操作系统（MacOS、Linux、BSD）中，您还可以通过以下方式之一安装它：

sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
sudo aria2c https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp --dir /usr/local/bin -o yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
画中画_
您可以使用以下命令安装PyPI 包：

python3 -m pip install -U yt-dlp
您可以在没有任何可选依赖项的情况下安装：

python3 -m pip install --no-deps -U yt-dlp
如果你想走在最前沿，你还可以安装 master 分支：

python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
在某些系统上，您可能需要使用pyorpython代替python3

用家酿
使用 Homebrew 的 macOS 或 Linux 用户也可以通过以下方式安装它：

brew install yt-dlp/taps/yt-dlp
更新
yt-dlp -U如果您使用提供的版本，您可以使用更新

如果您使用 pip 安装，只需重新运行用于安装程序的相同命令

如果您使用 Homebrew 安装，请运行brew upgrade yt-dlp/taps/yt-dlp

发布文件
推荐的
文件	描述
yt-dlp	独立于平台的zipimport二进制文件。需要 Python（推荐用于Linux/BSD）
yt-dlp.exe	Windows (Win7 SP1+) 独立 x64 二进制文件（推荐用于Windows）
yt-dlp_macos	通用 MacOS (10.15+) 独立可执行文件（推荐用于MacOS）
备择方案
文件	描述
yt-dlp_x86.exe	Windows (Vista SP2+) 独立 x86（32 位）二进制
yt-dlp_min.exe	Windows (Win7 SP1+) 独立 x64 二进制文件py2exe
（不推荐）
yt-dlp_linux	Linux 独立 x64 二进制文件
yt-dlp_linux.zip	未打包的 Linux 可执行文件（无自动更新）
yt-dlp_win.zip	未打包的 Windows 可执行文件（无自动更新）
yt-dlp_macos.zip	未打包的 MacOS (10.15+) 可执行文件（无自动更新）
yt-dlp_macos_legacy	MacOS (10.9+) 独立 x64 可执行文件
杂项
文件	描述
yt-dlp.tar.gz	源压缩包。还包含联机帮助页、完成等
SHA2-512SUMS	GNU 风格的 SHA512 和
SHA2-256SUMS	GNU 风格的 SHA256 和
依赖项
支持 Python 版本 3.7+（CPython 和 PyPy）。其他版本和实现可能会或可能不会正常工作。

虽然所有其他依赖项都是可选的，ffmpeg但ffprobe强烈推荐

强力推荐
ffmpeg和ffprobe - 用于合并单独的视频和音频文件以及各种后处理任务。许可证取决于构建

注意：在较新的 ffmpeg 版本中有一些回归，当与 yt-dlp 一起使用时会导致各种问题。由于 ffmpeg 是一个如此重要的依赖项，我们在yt-dlp/FFmpeg-Builds为这些问题提供了带有补丁的自定义构建。有关这些构建解决的具体问题的详细信息，请参阅自述文件

联网
certifi * - 提供 Mozilla 的根证书包。在MPLv2下
brotli * 或brotlicffi - Brotli内容编码支持。两者均获得 MIT 1 2许可
websockets * - 用于通过 websocket 下载。根据BSD-3-Clause 获得许可
元数据
mutagen * - 用于--embed-thumbnail某些格式。在GPLv2+下获得许可
AtomicParsley - 用于--embed-thumbnail/mp4文件m4a时mutagen/ffmpeg不能。在GPLv2+下获得许可
xattr、 pyxattr或setfattr - 用于在Linux上编写 xattr 元数据 (--xattr)。分别获得MIT、 LGPL2.1和GPLv2+许可
杂项
pycryptodomex * - 用于解密 AES-128 HLS 流和各种其他数据。根据BSD-2-Clause 获得许可
phantomjs - 用于需要运行 javascript 的提取器。根据BSD-3-Clause 获得许可
secretstorage - 用于在Linux上解密基于Chromium的浏览器的cookie 时--cookies-from-browser访问Gnome密钥环。根据BSD-3-Clause 获得许可
您要使用的任何外部下载器--downloader
已弃用
avconv和avprobe - 现在不推荐使用ffmpeg 的替代品。许可证取决于构建
sponskrub - 用于使用现已弃用的 sponskrub 选项。在GPLv3+下获得许可
rtmpdump - 用于下载rtmp流。ffmpeg 可以与--downloader ffmpeg. 在GPLv2+下获得许可
mplayer或mpv - 用于下载rstp/mms流。ffmpeg 可以与--downloader ffmpeg. 在GPLv2+下获得许可
要使用或重新分发依赖项，您必须同意它们各自的许可条款。

独立发布二进制文件是使用 Python 解释器构建的，并且包含标有*的包。

如果您对正在尝试的任务没有必要的依赖项，yt-dlp 会警告您。--verbose所有当前可用的依赖项都在输出顶部可见

编译
独立 PyInstaller 构建
要构建 Windows/MacOS 可执行文件，您必须拥有 Python 和pyinstaller（如果需要，还可以加上任何 yt-dlp 的可选依赖项）。安装完所有必要的依赖项后，只需运行pyinst.py. 可执行文件将针对与使用的 Python 相同的架构（32/64 位）构建。

python3 -m pip install -U pyinstaller -r requirements.txt
python3 devscripts/make_lazy_extractors.py
python3 pyinst.py
在某些系统上，您可能需要使用pyorpython而不是python3.

请注意，pyinstaller不支持在不使用虚拟环境的情况下从 Windows 商店安装 Python。

重要提示：官方不支持不使用直接pyinstaller运行。这可能会或可能不会正常工作。pyinst.py

独立于平台的二进制文件 (UNIX)
您将需要构建工具python(3.6+)、、zip( makeGNU)、pandoc* 和pytest*。

安装这些后，只需运行make.

您也可以make yt-dlp改为只编译二进制文件而不更新任何附加文件。（这里不需要标有*的依赖项）

独立 Py2Exe 构建 (Windows)
虽然我们提供了使用py2exe构建的选项，但建议使用 PyInstaller构建，因为 py2exe 构建不能包含pycryptodomex/certifi并且需要目标计算机上的 VC++14才能运行。

如果您仍然想构建它，请安装 Python 和 py2exe，然后简单地运行setup.py py2exe

py -m pip install -U py2exe -r requirements.txt
py devscripts/make_lazy_extractors.py
py setup.py py2exe
相关脚本
devscripts/update-version.py- 根据当前时间戳更新版本号
devscripts/make_lazy_extractors.py- 创建惰性提取器。在构建二进制文件（任何变体）之前运行它会提高它们的启动性能。YTDLP_NO_LAZY_EXTRACTORS=1如果您希望强制禁用延迟提取器加载，请设置环境变量。
您还可以在 github 上 fork 项目并运行 fork 的构建工作流程以自动构建完整版本

用法和选项
yt-dlp [OPTIONS] [--] URL [URL...]
Ctrl+F是你的朋友 :D

常规选项：
-h, --help                      Print this help text and exit
--version                       Print program version and exit
-U, --update                    Update this program to latest version
--no-update                     Do not update (default)
-i, --ignore-errors             Ignore download and postprocessing errors.
                                The download will be considered successful
                                even if the postprocessing fails
--no-abort-on-error             Continue with next video on download errors;
                                e.g. to skip unavailable videos in a
                                playlist (default)
--abort-on-error                Abort downloading of further videos if an
                                error occurs (Alias: --no-ignore-errors)
--dump-user-agent               Display the current user-agent and exit
--list-extractors               List all supported extractors and exit
--extractor-descriptions        Output descriptions of all supported
                                extractors and exit
--force-generic-extractor       Force extraction to use the generic extractor
--default-search PREFIX         Use this prefix for unqualified URLs. Eg:
                                "gvsearch2:python" downloads two videos from
                                google videos for the search term "python".
                                Use the value "auto" to let yt-dlp guess
                                ("auto_warning" to emit a warning when
                                guessing). "error" just throws an error. The
                                default value "fixup_error" repairs broken
                                URLs, but emits an error if this is not
                                possible instead of searching
--ignore-config                 Don't load any more configuration files
                                except those given by --config-locations.
                                For backward compatibility, if this option
                                is found inside the system configuration
                                file, the user configuration is not loaded.
                                (Alias: --no-config)
--no-config-locations           Do not load any custom configuration files
                                (default). When given inside a configuration
                                file, ignore all previous --config-locations
                                defined in the current file
--config-locations PATH         Location of the main configuration file;
                                either the path to the config or its
                                containing directory ("-" for stdin). Can be
                                used multiple times and inside other
                                configuration files
--flat-playlist                 Do not extract the videos of a playlist,
                                only list them
--no-flat-playlist              Extract the videos of a playlist
--live-from-start               Download livestreams from the start.
                                Currently only supported for YouTube
                                (Experimental)
--no-live-from-start            Download livestreams from the current time
                                (default)
--wait-for-video MIN[-MAX]      Wait for scheduled streams to become
                                available. Pass the minimum number of
                                seconds (or range) to wait between retries
--no-wait-for-video             Do not wait for scheduled streams (default)
--mark-watched                  Mark videos watched (even with --simulate)
--no-mark-watched               Do not mark videos watched (default)
--no-colors                     Do not emit color codes in output (Alias:
                                --no-colours)
--compat-options OPTS           Options that can help keep compatibility
                                with youtube-dl or youtube-dlc
                                configurations by reverting some of the
                                changes made in yt-dlp. See "Differences in
                                default behavior" for details
--alias ALIASES OPTIONS         Create aliases for an option string. Unless
                                an alias starts with a dash "-", it is
                                prefixed with "--". Arguments are parsed
                                according to the Python string formatting
                                mini-language. Eg: --alias get-audio,-X
                                "-S=aext:{0},abr -x --audio-format {0}"
                                creates options "--get-audio" and "-X" that
                                takes an argument (ARG0) and expands to
                                "-S=aext:ARG0,abr -x --audio-format ARG0".
                                All defined aliases are listed in the --help
                                output. Alias options can trigger more
                                aliases; so be careful to avoid defining
                                recursive options. As a safety measure, each
                                alias may be triggered a maximum of 100
                                times. This option can be used multiple times
网络选项：
--proxy URL                     Use the specified HTTP/HTTPS/SOCKS proxy. To
                                enable SOCKS proxy, specify a proper scheme.
                                Eg: socks5://user:pass@127.0.0.1:1080/. Pass
                                in an empty string (--proxy "") for direct
                                connection
--socket-timeout SECONDS        Time to wait before giving up, in seconds
--source-address IP             Client-side IP address to bind to
-4, --force-ipv4                Make all connections via IPv4
-6, --force-ipv6                Make all connections via IPv6
地理限制：
--geo-verification-proxy URL    Use this proxy to verify the IP address for
                                some geo-restricted sites. The default proxy
                                specified by --proxy (or none, if the option
                                is not present) is used for the actual
                                downloading
--geo-bypass                    Bypass geographic restriction via faking
                                X-Forwarded-For HTTP header (default)
--no-geo-bypass                 Do not bypass geographic restriction via
                                faking X-Forwarded-For HTTP header
--geo-bypass-country CODE       Force bypass geographic restriction with
                                explicitly provided two-letter ISO 3166-2
                                country code
--geo-bypass-ip-block IP_BLOCK  Force bypass geographic restriction with
                                explicitly provided IP block in CIDR notation
视频选择：
-I, --playlist-items ITEM_SPEC  Comma separated playlist_index of the videos
                                to download. You can specify a range using
                                "[START]:[STOP][:STEP]". For backward
                                compatibility, START-STOP is also supported.
                                Use negative indices to count from the right
                                and negative STEP to download in reverse
                                order. Eg: "-I 1:3,7,-5::2" used on a
                                playlist of size 15 will download the videos
                                at index 1,2,3,7,11,13,15
--min-filesize SIZE             Do not download any videos smaller than SIZE
                                (e.g. 50k or 44.6m)
--max-filesize SIZE             Do not download any videos larger than SIZE
                                (e.g. 50k or 44.6m)
--date DATE                     Download only videos uploaded on this date.
                                The date can be "YYYYMMDD" or in the format 
                                [now|today|yesterday][-N[day|week|month|year]].
                                Eg: --date today-2weeks
--datebefore DATE               Download only videos uploaded on or before
                                this date. The date formats accepted is the
                                same as --date
--dateafter DATE                Download only videos uploaded on or after
                                this date. The date formats accepted is the
                                same as --date
--match-filters FILTER          Generic video filter. Any "OUTPUT TEMPLATE"
                                field can be compared with a number or a
                                string using the operators defined in
                                "Filtering Formats". You can also simply
                                specify a field to match if the field is
                                present, use "!field" to check if the field
                                is not present, and "&" to check multiple
                                conditions. Use a "\" to escape "&" or
                                quotes if needed. If used multiple times,
                                the filter matches if atleast one of the
                                conditions are met. Eg: --match-filter
                                !is_live --match-filter "like_count>?100 &
                                description~='(?i)\bcats \& dogs\b'" matches
                                only videos that are not live OR those that
                                have a like count more than 100 (or the like
                                field is not available) and also has a
                                description that contains the phrase "cats &
                                dogs" (caseless). Use "--match-filter -" to
                                interactively ask whether to download each
                                video
--no-match-filter               Do not use generic video filter (default)
--no-playlist                   Download only the video, if the URL refers
                                to a video and a playlist
--yes-playlist                  Download the playlist, if the URL refers to
                                a video and a playlist
--age-limit YEARS               Download only videos suitable for the given
                                age
--download-archive FILE         Download only videos not listed in the
                                archive file. Record the IDs of all
                                downloaded videos in it
--no-download-archive           Do not use archive file (default)
--max-downloads NUMBER          Abort after downloading NUMBER files
--break-on-existing             Stop the download process when encountering
                                a file that is in the archive
--break-on-reject               Stop the download process when encountering
                                a file that has been filtered out
--break-per-input               Make --break-on-existing, --break-on-reject
                                and --max-downloads act only on the current
                                input URL
--no-break-per-input            --break-on-existing and similar options
                                terminates the entire download queue
--skip-playlist-after-errors N  Number of allowed failures until the rest of
                                the playlist is skipped
下载选项：
-N, --concurrent-fragments N    Number of fragments of a dash/hlsnative
                                video that should be downloaded concurrently
                                (default is 1)
-r, --limit-rate RATE           Maximum download rate in bytes per second
                                (e.g. 50K or 4.2M)
--throttled-rate RATE           Minimum download rate in bytes per second
                                below which throttling is assumed and the
                                video data is re-extracted (e.g. 100K)
-R, --retries RETRIES           Number of retries (default is 10), or
                                "infinite"
--file-access-retries RETRIES   Number of times to retry on file access
                                error (default is 3), or "infinite"
--fragment-retries RETRIES      Number of retries for a fragment (default is
                                10), or "infinite" (DASH, hlsnative and ISM)
--retry-sleep [TYPE:]EXPR       Time to sleep between retries in seconds
                                (optionally) prefixed by the type of retry
                                (http (default), fragment, file_access,
                                extractor) to apply the sleep to. EXPR can
                                be a number, linear=START[:END[:STEP=1]] or
                                exp=START[:END[:BASE=2]]. This option can be
                                used multiple times to set the sleep for the
                                different retry types. Eg: --retry-sleep
                                linear=1::2 --retry-sleep fragment:exp=1:20
--skip-unavailable-fragments    Skip unavailable fragments for DASH,
                                hlsnative and ISM downloads (default)
                                (Alias: --no-abort-on-unavailable-fragment)
--abort-on-unavailable-fragment
                                Abort download if a fragment is unavailable
                                (Alias: --no-skip-unavailable-fragments)
--keep-fragments                Keep downloaded fragments on disk after
                                downloading is finished
--no-keep-fragments             Delete downloaded fragments after
                                downloading is finished (default)
--buffer-size SIZE              Size of download buffer (e.g. 1024 or 16K)
                                (default is 1024)
--resize-buffer                 The buffer size is automatically resized
                                from an initial value of --buffer-size
                                (default)
--no-resize-buffer              Do not automatically adjust the buffer size
--http-chunk-size SIZE          Size of a chunk for chunk-based HTTP
                                downloading (e.g. 10485760 or 10M) (default
                                is disabled). May be useful for bypassing
                                bandwidth throttling imposed by a webserver
                                (experimental)
--playlist-random               Download playlist videos in random order
--lazy-playlist                 Process entries in the playlist as they are
                                received. This disables n_entries,
                                --playlist-random and --playlist-reverse
--no-lazy-playlist              Process videos in the playlist only after
                                the entire playlist is parsed (default)
--xattr-set-filesize            Set file xattribute ytdl.filesize with
                                expected file size
--hls-use-mpegts                Use the mpegts container for HLS videos;
                                allowing some players to play the video
                                while downloading, and reducing the chance
                                of file corruption if download is
                                interrupted. This is enabled by default for
                                live streams
--no-hls-use-mpegts             Do not use the mpegts container for HLS
                                videos. This is default when not downloading
                                live streams
--download-sections REGEX       Download only chapters whose title matches
                                the given regular expression. Time ranges
                                prefixed by a "*" can also be used in place
                                of chapters to download the specified range.
                                Eg: --download-sections "*10:15-15:00"
                                --download-sections "intro". Needs ffmpeg.
                                This option can be used multiple times to
                                download multiple sections
--downloader [PROTO:]NAME       Name or path of the external downloader to
                                use (optionally) prefixed by the protocols
                                (http, ftp, m3u8, dash, rstp, rtmp, mms) to
                                use it for. Currently supports native,
                                aria2c, avconv, axel, curl, ffmpeg, httpie,
                                wget. You can use this option multiple times
                                to set different downloaders for different
                                protocols. For example, --downloader aria2c
                                --downloader "dash,m3u8:native" will use
                                aria2c for http/ftp downloads, and the
                                native downloader for dash/m3u8 downloads
                                (Alias: --external-downloader)
--downloader-args NAME:ARGS     Give these arguments to the external
                                downloader. Specify the downloader name and
                                the arguments separated by a colon ":". For
                                ffmpeg, arguments can be passed to different
                                positions using the same syntax as
                                --postprocessor-args. You can use this
                                option multiple times to give different
                                arguments to different downloaders (Alias:
                                --external-downloader-args)
文件系统选项：
-a, --batch-file FILE           File containing URLs to download ("-" for
                                stdin), one URL per line. Lines starting
                                with "#", ";" or "]" are considered as
                                comments and ignored
--no-batch-file                 Do not read URLs from batch file (default)
-P, --paths [TYPES:]PATH        The paths where the files should be
                                downloaded. Specify the type of file and the
                                path separated by a colon ":". All the same
                                TYPES as --output are supported.
                                Additionally, you can also provide "home"
                                (default) and "temp" paths. All intermediary
                                files are first downloaded to the temp path
                                and then the final files are moved over to
                                the home path after download is finished.
                                This option is ignored if --output is an
                                absolute path
-o, --output [TYPES:]TEMPLATE   Output filename template; see "OUTPUT
                                TEMPLATE" for details
--output-na-placeholder TEXT    Placeholder for unavailable fields in
                                "OUTPUT TEMPLATE" (default: "NA")
--restrict-filenames            Restrict filenames to only ASCII characters,
                                and avoid "&" and spaces in filenames
--no-restrict-filenames         Allow Unicode characters, "&" and spaces in
                                filenames (default)
--windows-filenames             Force filenames to be Windows-compatible
--no-windows-filenames          Make filenames Windows-compatible only if
                                using Windows (default)
--trim-filenames LENGTH         Limit the filename length (excluding
                                extension) to the specified number of
                                characters
-w, --no-overwrites             Do not overwrite any files
--force-overwrites              Overwrite all video and metadata files. This
                                option includes --no-continue
--no-force-overwrites           Do not overwrite the video, but overwrite
                                related files (default)
-c, --continue                  Resume partially downloaded files/fragments
                                (default)
--no-continue                   Do not resume partially downloaded
                                fragments. If the file is not fragmented,
                                restart download of the entire file
--part                          Use .part files instead of writing directly
                                into output file (default)
--no-part                       Do not use .part files - write directly into
                                output file
--mtime                         Use the Last-modified header to set the file
                                modification time (default)
--no-mtime                      Do not use the Last-modified header to set
                                the file modification time
--write-description             Write video description to a .description file
--no-write-description          Do not write video description (default)
--write-info-json               Write video metadata to a .info.json file
                                (this may contain personal information)
--no-write-info-json            Do not write video metadata (default)
--write-playlist-metafiles      Write playlist metadata in addition to the
                                video metadata when using --write-info-json,
                                --write-description etc. (default)
--no-write-playlist-metafiles   Do not write playlist metadata when using
                                --write-info-json, --write-description etc.
--clean-info-json               Remove some private fields such as filenames
                                from the infojson. Note that it could still
                                contain some personal information (default)
--no-clean-info-json            Write all fields to the infojson
--write-comments                Retrieve video comments to be placed in the
                                infojson. The comments are fetched even
                                without this option if the extraction is
                                known to be quick (Alias: --get-comments)
--no-write-comments             Do not retrieve video comments unless the
                                extraction is known to be quick (Alias:
                                --no-get-comments)
--load-info-json FILE           JSON file containing the video information
                                (created with the "--write-info-json" option)
--cookies FILE                  Netscape formatted file to read cookies from
                                and dump cookie jar in
--no-cookies                    Do not read/dump cookies from/to file
                                (default)
--cookies-from-browser BROWSER[+KEYRING][:PROFILE]
                                The name of the browser and (optionally) the
                                name/path of the profile to load cookies
                                from, separated by a ":". Currently
                                supported browsers are: brave, chrome,
                                chromium, edge, firefox, opera, safari,
                                vivaldi. By default, the most recently
                                accessed profile is used. The keyring used
                                for decrypting Chromium cookies on Linux can
                                be (optionally) specified after the browser
                                name separated by a "+". Currently supported
                                keyrings are: basictext, gnomekeyring, kwallet
--no-cookies-from-browser       Do not load cookies from browser (default)
--cache-dir DIR                 Location in the filesystem where youtube-dl
                                can store some downloaded information (such
                                as client ids and signatures) permanently.
                                By default $XDG_CACHE_HOME/yt-dlp or
                                ~/.cache/yt-dlp
--no-cache-dir                  Disable filesystem caching
--rm-cache-dir                  Delete all filesystem cache files
缩略图选项：
--write-thumbnail               Write thumbnail image to disk
--no-write-thumbnail            Do not write thumbnail image to disk (default)
--write-all-thumbnails          Write all thumbnail image formats to disk
--list-thumbnails               List available thumbnails of each video.
                                Simulate unless --no-simulate is used
互联网快捷方式选项：
--write-link                    Write an internet shortcut file, depending
                                on the current platform (.url, .webloc or
                                .desktop). The URL may be cached by the OS
--write-url-link                Write a .url Windows internet shortcut. The
                                OS caches the URL based on the file path
--write-webloc-link             Write a .webloc macOS internet shortcut
--write-desktop-link            Write a .desktop Linux internet shortcut
详细程度和模拟选项：
-q, --quiet                     Activate quiet mode. If used with --verbose,
                                print the log to stderr
--no-warnings                   Ignore warnings
-s, --simulate                  Do not download the video and do not write
                                anything to disk
--no-simulate                   Download the video even if printing/listing
                                options are used
--ignore-no-formats-error       Ignore "No video formats" error. Useful for
                                extracting metadata even if the videos are
                                not actually available for download
                                (experimental)
--no-ignore-no-formats-error    Throw error when no downloadable video
                                formats are found (default)
--skip-download                 Do not download the video but write all
                                related files (Alias: --no-download)
-O, --print [WHEN:]TEMPLATE     Field name or output template to print to
                                screen, optionally prefixed with when to
                                print it, separated by a ":". Supported
                                values of "WHEN" are the same as that of
                                --use-postprocessor, and "video" (default).
                                Implies --quiet. Implies --simulate unless
                                --no-simulate or later stages of WHEN are
                                used. This option can be used multiple times
--print-to-file [WHEN:]TEMPLATE FILE
                                Append given template to the file. The
                                values of WHEN and TEMPLATE are same as that
                                of --print. FILE uses the same syntax as the
                                output template. This option can be used
                                multiple times
-j, --dump-json                 Quiet, but print JSON information for each
                                video. Simulate unless --no-simulate is
                                used. See "OUTPUT TEMPLATE" for a
                                description of available keys
-J, --dump-single-json          Quiet, but print JSON information for each
                                url or infojson passed. Simulate unless
                                --no-simulate is used. If the URL refers to
                                a playlist, the whole playlist information
                                is dumped in a single line
--force-write-archive           Force download archive entries to be written
                                as far as no errors occur, even if -s or
                                another simulation option is used (Alias:
                                --force-download-archive)
--newline                       Output progress bar as new lines
--no-progress                   Do not print progress bar
--progress                      Show progress bar, even if in quiet mode
--console-title                 Display progress in console titlebar
--progress-template [TYPES:]TEMPLATE
                                Template for progress outputs, optionally
                                prefixed with one of "download:" (default),
                                "download-title:" (the console title),
                                "postprocess:",  or "postprocess-title:".
                                The video's fields are accessible under the
                                "info" key and the progress attributes are
                                accessible under "progress" key. E.g.:
                                --console-title --progress-template
                                "download-title:%(info.id)s-%(progress.eta)s"
-v, --verbose                   Print various debugging information
--dump-pages                    Print downloaded pages encoded using base64
                                to debug problems (very verbose)
--write-pages                   Write downloaded intermediary pages to files
                                in the current directory to debug problems
--print-traffic                 Display sent and read HTTP traffic
解决方法：
--encoding ENCODING             Force the specified encoding (experimental)
--legacy-server-connect         Explicitly allow HTTPS connection to servers
                                that do not support RFC 5746 secure
                                renegotiation
--no-check-certificates         Suppress HTTPS certificate validation
--prefer-insecure               Use an unencrypted connection to retrieve
                                information about the video (Currently
                                supported only for YouTube)
--add-header FIELD:VALUE        Specify a custom HTTP header and its value,
                                separated by a colon ":". You can use this
                                option multiple times
--bidi-workaround               Work around terminals that lack
                                bidirectional text support. Requires bidiv
                                or fribidi executable in PATH
--sleep-requests SECONDS        Number of seconds to sleep between requests
                                during data extraction
--sleep-interval SECONDS        Number of seconds to sleep before each
                                download. This is the minimum time to sleep
                                when used along with --max-sleep-interval
                                (Alias: --min-sleep-interval)
--max-sleep-interval SECONDS    Maximum number of seconds to sleep. Can only
                                be used along with --min-sleep-interval
--sleep-subtitles SECONDS       Number of seconds to sleep before each
                                subtitle download
视频格式选项：
-f, --format FORMAT             Video format code, see "FORMAT SELECTION"
                                for more details
-S, --format-sort SORTORDER     Sort the formats by the fields given, see
                                "Sorting Formats" for more details
--format-sort-force             Force user specified sort order to have
                                precedence over all fields, see "Sorting
                                Formats" for more details (Alias: --S-force)
--no-format-sort-force          Some fields have precedence over the user
                                specified sort order (default)
--video-multistreams            Allow multiple video streams to be merged
                                into a single file
--no-video-multistreams         Only one video stream is downloaded for each
                                output file (default)
--audio-multistreams            Allow multiple audio streams to be merged
                                into a single file
--no-audio-multistreams         Only one audio stream is downloaded for each
                                output file (default)
--prefer-free-formats           Prefer video formats with free containers
                                over non-free ones of same quality. Use with
                                "-S ext" to strictly prefer free containers
                                irrespective of quality
--no-prefer-free-formats        Don't give any special preference to free
                                containers (default)
--check-formats                 Make sure formats are selected only from
                                those that are actually downloadable
--check-all-formats             Check all formats for whether they are
                                actually downloadable
--no-check-formats              Do not check that the formats are actually
                                downloadable
-F, --list-formats              List available formats of each video.
                                Simulate unless --no-simulate is used
--merge-output-format FORMAT    Containers that may be used when merging
                                formats, separated by "/" (Eg: "mp4/mkv").
                                Ignored if no merge is required. (currently
                                supported: avi, flv, mkv, mov, mp4, webm)
字幕选项：
--write-subs                    Write subtitle file
--no-write-subs                 Do not write subtitle file (default)
--write-auto-subs               Write automatically generated subtitle file
                                (Alias: --write-automatic-subs)
--no-write-auto-subs            Do not write auto-generated subtitles
                                (default) (Alias: --no-write-automatic-subs)
--list-subs                     List available subtitles of each video.
                                Simulate unless --no-simulate is used
--sub-format FORMAT             Subtitle format; accepts formats preference,
                                Eg: "srt" or "ass/srt/best"
--sub-langs LANGS               Languages of the subtitles to download (can
                                be regex) or "all" separated by commas. (Eg:
                                --sub-langs "en.*,ja") You can prefix the
                                language code with a "-" to exclude it from
                                the requested languages. (Eg: --sub-langs
                                all,-live_chat) Use --list-subs for a list
                                of available language tags
身份验证选项：
-u, --username USERNAME         Login with this account ID
-p, --password PASSWORD         Account password. If this option is left
                                out, yt-dlp will ask interactively
-2, --twofactor TWOFACTOR       Two-factor authentication code
-n, --netrc                     Use .netrc authentication data
--netrc-location PATH           Location of .netrc authentication data;
                                either the path or its containing directory.
                                Defaults to ~/.netrc
--video-password PASSWORD       Video password (vimeo, youku)
--ap-mso MSO                    Adobe Pass multiple-system operator (TV
                                provider) identifier, use --ap-list-mso for
                                a list of available MSOs
--ap-username USERNAME          Multiple-system operator account login
--ap-password PASSWORD          Multiple-system operator account password.
                                If this option is left out, yt-dlp will ask
                                interactively
--ap-list-mso                   List all supported multiple-system operators
--client-certificate CERTFILE   Path to client certificate file in PEM
                                format. May include the private key
--client-certificate-key KEYFILE
                                Path to private key file for client
                                certificate
--client-certificate-password PASSWORD
                                Password for client certificate private key,
                                if encrypted. If not provided, and the key
                                is encrypted, yt-dlp will ask interactively
后处理选项：
-x, --extract-audio             Convert video files to audio-only files
                                (requires ffmpeg and ffprobe)
--audio-format FORMAT           Format to convert the audio to when -x is
                                used. (currently supported: best (default),
                                aac, alac, flac, m4a, mp3, opus, vorbis,
                                wav). You can specify multiple rules using
                                similar syntax as --remux-video
--audio-quality QUALITY         Specify ffmpeg audio quality to use when
                                converting the audio with -x. Insert a value
                                between 0 (best) and 10 (worst) for VBR or a
                                specific bitrate like 128K (default 5)
--remux-video FORMAT            Remux the video into another container if
                                necessary (currently supported: avi, flv,
                                mkv, mov, mp4, webm, aac, aiff, alac, flac,
                                m4a, mka, mp3, ogg, opus, vorbis, wav). If
                                target container does not support the
                                video/audio codec, remuxing will fail. You
                                can specify multiple rules; Eg.
                                "aac>m4a/mov>mp4/mkv" will remux aac to m4a,
                                mov to mp4 and anything else to mkv
--recode-video FORMAT           Re-encode the video into another format if
                                necessary. The syntax and supported formats
                                are the same as --remux-video
--postprocessor-args NAME:ARGS  Give these arguments to the postprocessors.
                                Specify the postprocessor/executable name
                                and the arguments separated by a colon ":"
                                to give the argument to the specified
                                postprocessor/executable. Supported PP are:
                                Merger, ModifyChapters, SplitChapters,
                                ExtractAudio, VideoRemuxer, VideoConvertor,
                                Metadata, EmbedSubtitle, EmbedThumbnail,
                                SubtitlesConvertor, ThumbnailsConvertor,
                                FixupStretched, FixupM4a, FixupM3u8,
                                FixupTimestamp and FixupDuration. The
                                supported executables are: AtomicParsley,
                                FFmpeg and FFprobe. You can also specify
                                "PP+EXE:ARGS" to give the arguments to the
                                specified executable only when being used by
                                the specified postprocessor. Additionally,
                                for ffmpeg/ffprobe, "_i"/"_o" can be
                                appended to the prefix optionally followed
                                by a number to pass the argument before the
                                specified input/output file. Eg: --ppa
                                "Merger+ffmpeg_i1:-v quiet". You can use
                                this option multiple times to give different
                                arguments to different postprocessors.
                                (Alias: --ppa)
-k, --keep-video                Keep the intermediate video file on disk
                                after post-processing
--no-keep-video                 Delete the intermediate video file after
                                post-processing (default)
--post-overwrites               Overwrite post-processed files (default)
--no-post-overwrites            Do not overwrite post-processed files
--embed-subs                    Embed subtitles in the video (only for mp4,
                                webm and mkv videos)
--no-embed-subs                 Do not embed subtitles (default)
--embed-thumbnail               Embed thumbnail in the video as cover art
--no-embed-thumbnail            Do not embed thumbnail (default)
--embed-metadata                Embed metadata to the video file. Also
                                embeds chapters/infojson if present unless
                                --no-embed-chapters/--no-embed-info-json are
                                used (Alias: --add-metadata)
--no-embed-metadata             Do not add metadata to file (default)
                                (Alias: --no-add-metadata)
--embed-chapters                Add chapter markers to the video file
                                (Alias: --add-chapters)
--no-embed-chapters             Do not add chapter markers (default) (Alias:
                                --no-add-chapters)
--embed-info-json               Embed the infojson as an attachment to
                                mkv/mka video files
--no-embed-info-json            Do not embed the infojson as an attachment
                                to the video file
--parse-metadata FROM:TO        Parse additional metadata like title/artist
                                from other fields; see "MODIFYING METADATA"
                                for details
--replace-in-metadata FIELDS REGEX REPLACE
                                Replace text in a metadata field using the
                                given regex. This option can be used
                                multiple times
--xattrs                        Write metadata to the video file's xattrs
                                (using dublin core and xdg standards)
--concat-playlist POLICY        Concatenate videos in a playlist. One of
                                "never", "always", or "multi_video"
                                (default; only when the videos form a single
                                show). All the video files must have same
                                codecs and number of streams to be
                                concatable. The "pl_video:" prefix can be
                                used with "--paths" and "--output" to set
                                the output filename for the concatenated
                                files. See "OUTPUT TEMPLATE" for details
--fixup POLICY                  Automatically correct known faults of the
                                file. One of never (do nothing), warn (only
                                emit a warning), detect_or_warn (the
                                default; fix file if we can, warn
                                otherwise), force (try fixing even if file
                                already exists)
--ffmpeg-location PATH          Location of the ffmpeg binary; either the
                                path to the binary or its containing directory
--exec [WHEN:]CMD               Execute a command, optionally prefixed with
                                when to execute it (after_move if
                                unspecified), separated by a ":". Supported
                                values of "WHEN" are the same as that of
                                --use-postprocessor. Same syntax as the
                                output template can be used to pass any
                                field as arguments to the command. After
                                download, an additional field "filepath"
                                that contains the final path of the
                                downloaded file is also available, and if no
                                fields are passed, %(filepath)q is appended
                                to the end of the command. This option can
                                be used multiple times
--no-exec                       Remove any previously defined --exec
--convert-subs FORMAT           Convert the subtitles to another format
                                (currently supported: ass, lrc, srt, vtt)
                                (Alias: --convert-subtitles)
--convert-thumbnails FORMAT     Convert the thumbnails to another format
                                (currently supported: jpg, png, webp). You
                                can specify multiple rules using similar
                                syntax as --remux-video
--split-chapters                Split video into multiple files based on
                                internal chapters. The "chapter:" prefix can
                                be used with "--paths" and "--output" to set
                                the output filename for the split files. See
                                "OUTPUT TEMPLATE" for details
--no-split-chapters             Do not split video based on chapters (default)
--remove-chapters REGEX         Remove chapters whose title matches the
                                given regular expression. The syntax is the
                                same as --download-sections. This option can
                                be used multiple times
--no-remove-chapters            Do not remove any chapters from the file
                                (default)
--force-keyframes-at-cuts       Force keyframes at cuts when
                                downloading/splitting/removing sections.
                                This is slow due to needing a re-encode, but
                                the resulting video may have fewer artifacts
                                around the cuts
--no-force-keyframes-at-cuts    Do not force keyframes around the chapters
                                when cutting/splitting (default)
--use-postprocessor NAME[:ARGS]
                                The (case sensitive) name of plugin
                                postprocessors to be enabled, and
                                (optionally) arguments to be passed to it,
                                separated by a colon ":". ARGS are a
                                semicolon ";" delimited list of NAME=VALUE.
                                The "when" argument determines when the
                                postprocessor is invoked. It can be one of
                                "pre_process" (after video extraction),
                                "after_filter" (after video passes filter),
                                "before_dl" (before each video download),
                                "post_process" (after each video download;
                                default), "after_move" (after moving video
                                file to it's final locations), "after_video"
                                (after downloading and processing all
                                formats of a video), or "playlist" (at end
                                of playlist). This option can be used
                                multiple times to add different postprocessors
赞助商区块选项：
使用SponsorBlock API为下载的 YouTube 视频制作章节条目或删除各种片段（赞助商、介绍等）

--sponsorblock-mark CATS        SponsorBlock categories to create chapters
                                for, separated by commas. Available
                                categories are sponsor, intro, outro,
                                selfpromo, preview, filler, interaction,
                                music_offtopic, poi_highlight, all and
                                default (=all). You can prefix the category
                                with a "-" to exclude it. See [1] for
                                description of the categories. Eg:
                                --sponsorblock-mark all,-preview
                                [1] https://wiki.sponsor.ajay.app/w/Segment_Categories
--sponsorblock-remove CATS      SponsorBlock categories to be removed from
                                the video file, separated by commas. If a
                                category is present in both mark and remove,
                                remove takes precedence. The syntax and
                                available categories are the same as for
                                --sponsorblock-mark except that "default"
                                refers to "all,-filler" and poi_highlight is
                                not available
--sponsorblock-chapter-title TEMPLATE
                                An output template for the title of the
                                SponsorBlock chapters created by
                                --sponsorblock-mark. The only available
                                fields are start_time, end_time, category,
                                categories, name, category_names. Defaults
                                to "[SponsorBlock]: %(category_names)l"
--no-sponsorblock               Disable both --sponsorblock-mark and
                                --sponsorblock-remove
--sponsorblock-api URL          SponsorBlock API location, defaults to
                                https://sponsor.ajay.app
提取器选项：
--extractor-retries RETRIES     Number of retries for known extractor errors
                                (default is 3), or "infinite"
--allow-dynamic-mpd             Process dynamic DASH manifests (default)
                                (Alias: --no-ignore-dynamic-mpd)
--ignore-dynamic-mpd            Do not process dynamic DASH manifests
                                (Alias: --no-allow-dynamic-mpd)
--hls-split-discontinuity       Split HLS playlists to different formats at
                                discontinuities such as ad breaks
--no-hls-split-discontinuity    Do not split HLS playlists to different
                                formats at discontinuities such as ad breaks
                                (default)
--extractor-args KEY:ARGS       Pass these arguments to the extractor. See
                                "EXTRACTOR ARGUMENTS" for details. You can
                                use this option multiple times to give
                                arguments for different extractors
配置
您可以通过将任何受支持的命令行选项放入配置文件来配置 yt-dlp。配置从以下位置加载：

主要配置：文件由--config-location

可移植配置：yt-dlp.conf与捆绑的二进制文件在同一目录中。如果您从源代码 ( <root dir>/yt_dlp/__main__.py) 运行，则使用根目录。

主配置：yt-dlp.conf在由给出的主路径-P中，如果没有给出这样的路径，则在当前目录中

用户配置：

%XDG_CONFIG_HOME%/yt-dlp/config（推荐在 Linux/macOS 上使用）
%XDG_CONFIG_HOME%/yt-dlp.conf
%APPDATA%/yt-dlp/config（建议在 Windows 上使用）
%APPDATA%/yt-dlp/config.txt
~/yt-dlp.conf
~/yt-dlp.conf.txt
%XDG_CONFIG_HOME%默认为~/.config如果未定义。在 windows 上，%APPDATA%一般 指向C:\Users\<user name>\AppData\Roaming和~指向%HOME%如果存在，%USERPROFILE%（一般C:\Users\<user name>），或%HOMEDRIVE%%HOMEPATH%

系统配置：/etc/yt-dlp.conf

例如，使用以下配置文件 yt-dlp 将始终提取音频，而不是复制 mtime，使用代理并将所有视频保存YouTube在您的主目录中的目录下：

# Lines starting with # are comments

# Always extract audio
-x

# Do not copy the mtime
--no-mtime

# Use this proxy
--proxy 127.0.0.1:3128

# Save all videos under YouTube directory in your home directory
-o ~/YouTube/%(title)s.%(ext)s
请注意，配置文件中的选项与常规命令行调用中使用的选项（即开关）相同；因此or之后不能有空格，例如or但不是or 。----o--proxy- o-- proxy

--ignore-config如果要禁用特定 yt-dlp 运行的所有配置文件，则可以使用。如果--ignore-config在任何配置文件中找到，则不会加载进一步的配置。例如，在可移植配置文件中具有该选项可防止加载家庭、用户和系统配置。此外，（为了向后兼容）如果--ignore-config在系统配置文件中找到，则不会加载用户配置。

配置文件编码
配置文件根据 UTF BOM（如果存在）进行解码，否则根据系统语言环境的编码进行解码。

如果您希望对文件进行不同的解码，请添加# coding: ENCODING到文件的开头（例如# coding: shift-jis）。在此之前不能有任何字符，即使是空格或 BOM。

.netrc文件认证
您可能还希望为支持身份验证的提取器配置自动凭据存储（通过使用 and 提供登录名和密码--username）--password，以便在每次 yt-dlp 执行时不将凭据作为命令行参数传递，并防止在 shell 命令历史记录中跟踪纯文本密码. 您可以在每个提取器的基础上使用.netrc文件来实现此目的。为此，您需要在其中创建一个.netrc文件--netrc-location并限制仅由您读取/写入的权限：

touch $HOME/.netrc
chmod a-rwx,u+rw $HOME/.netrc
之后，您可以按以下格式为提取器添加凭据，其中提取器是提取器的小写名称：

machine <extractor> login <username> password <password>
例如：

machine youtube login myaccount@gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
要使用文件激活身份验证，.netrc您应该将其传递--netrc给 yt-dlp 或将其放在配置文件中。

.netrc 文件的默认位置是UNIX 中的$HOME( ~)。在 Windows 上，%HOME%如果存在，%USERPROFILE%（通常C:\Users\<user name>）或%HOMEDRIVE%%HOMEPATH%

输出模板
该-o选项用于指示输出文件名的模板，而-P选项用于指定每种类型的文件应保存到的路径。

tl; dr： 导航到示例。

最简单的用法-o是在下载单个文件时不设置任何模板参数，例如（不yt-dlp -o funny_video.flv "https://some/video"建议使用像这样的硬编码文件扩展名，这可能会破坏一些后处理）。

但是，它也可能包含在下载每个视频时将被替换的特殊序列。特殊序列可以根据Python 字符串格式化操作进行格式化。例如，%(NAME)s或%(NAME)05d。为了澄清，这是一个百分比符号，后跟括号中的名称，然后是格式化操作。

字段名称本身（括号内的部分）也可以有一些特殊的格式：

对象遍历：元数据中可用的字典和列表可以使用.（点）分隔符进行遍历。您还可以使用:. 例如：%(tags.0)s, %(subtitles.en.-1.ext)s, %(id.3:7:-1)s, %(formats.:.format_id)s. %()s指整个infodict。请注意，使用此方法可用的所有字段都未在下面列出。用于-j查看此类字段

加法：数字字段的加法和减法可以分别使用+和来完成-。例如：%(playlist_index+10)03d,%(n_entries+1-playlist_index)d

日期/时间格式：日期/时间字段可以根据strftime 格式进行格式化，方法是使用>. 例如：%(duration>%H-%M-%S)s, %(upload_date>%Y-%m-%d)s,%(epoch-3600>%H-%M-%S)s

备选方案：可以指定备选字段，用 . 分隔,。例如：%(release_date>%Y,upload_date>%Y|Unknown)s

Replacement：可以使用&分隔符指定替换值。如果该字段不为空，则将使用此替换值代替实际的字段内容。这是在考虑了备用字段之后完成的；因此，如果任何替代字段不为空，则使用替换。

默认值：当字段为空时，可以使用|分隔符指定文字默认值。这会覆盖--output-na-template. 例如：%(uploader|Unknown)s

更多转换：除了普通格式类型diouxXeEfFgGcrs之外，yt-dlp 还支持转换为B= B ytes、j= j son（#漂亮打印的标志）、h= HTML 转义、l= 逗号分隔的list# （换行分隔的标志\n） , =用于终端q的字符串q# （用于将列表拆分为不同参数的标志），D= 添加D小数后缀（例如：10M）（#使用 1024 作为因子的标志），以及S=作为文件名的S anitize（#用于受限的标志）

Unicode 规范化：格式类型U可用于 NFC Unicode 规范化。替代形式标志 ( #) 将规范化更改为 NFD，并且转换标志+可用于 NFKC/NFKD 兼容性等价规范化。例如：%(title)+.100U是 NFKC

总而言之，字段的一般语法是：

%(name[.keys][addition][>strf][,alternate][&replacement][|default])[flags][width][.precision][length]type
此外，您可以通过指定文件类型，后跟以冒号分隔的模板，为各种元数据文件设置不同的输出模板，与通用输出模板分开:。支持的不同文件类型是subtitle, thumbnail, description, annotation（已弃用）, infojson, link, pl_thumbnail, pl_description, pl_infojson, chapter, pl_video. 例如，-o "%(title)s.%(ext)s" -o "thumbnail:%(title)s\%(title)s.%(ext)s" 将缩略图放在与视频同名的文件夹中。如果任何模板为空，则不会写入该类型的文件。例如：--write-thumbnail -o "thumbnail:"将为播放列表而不是视频编写缩略图。

可用的字段是：

id（字符串）：视频标识符
title（字符串）：视频标题
fulltitle（字符串）：忽略实时时间戳和通用标题的视频标题
url（字符串）：视频网址
ext（字符串）：视频文件扩展名
alt_title（字符串）：视频的次要标题
description（字符串）：视频的描述
display_id（字符串）：视频的替代标识符
uploader（字符串）：视频上传者的全名
license（字符串）：视频许可的许可名称
creator（字符串）：视频的创建者
timestamp（数字）：视频可用时刻的 UNIX 时间戳
upload_date（字符串）：UTC 格式的视频上传日期 (YYYYMMDD)
release_timestamp（数字）：视频发布时刻的 UNIX 时间戳
release_date（字符串）：视频发布的日期（YYYYMMDD），UTC
modified_timestamp（数字）：视频最后修改时刻的 UNIX 时间戳
modified_date（字符串）：视频最后一次修改的日期（YYYYMMDD），UTC
uploader_id（字符串）：视频上传者的昵称或 ID
channel(string): 上传视频的频道全名
channel_id（字符串）：频道 ID
channel_follower_count（数字）：频道的关注者数量
location（字符串）：拍摄视频的物理位置
duration（数字）：视频的长度（以秒为单位）
duration_string(string): 视频长度 (HH:mm:ss)
view_count（数字）：有多少用户在平台上观看了视频
like_count（数字）：视频的正面评价数
dislike_count（数字）：视频的负面评价数
repost_count（数字）：视频的转发次数
average_rating（数字）：用户给出的平均评分，使用的比例取决于网页
comment_count（数字）：视频的评论数（对于某些提取器，评论仅在末尾下载，因此无法使用此字段）
age_limit（数字）：视频的年龄限制（年）
live_status（字符串）：“not_live”、“is_live”、“is_upcoming”、“was_live”、“post_live”之一（已直播，但 VOD 尚未处理）
is_live（布尔值）：此视频是直播视频还是定长视频
was_live（布尔值）：此视频最初是否为直播
playable_in_embed(string): 是否允许此视频在其他网站的嵌入式播放器中播放
availability（字符串）：视频是“private”、“premium_only”、“subscriber_only”、“needs_auth”、“unlisted”还是“public”
start_time（数字）：应开始复制的时间（以秒为单位），如 URL 中所指定
end_time（数字）：复制应结束的时间（以秒为单位），如 URL 中所指定
format（字符串）：格式的人类可读描述
format_id（字符串）：由指定的格式代码--format
format_note（字符串）：有关格式的附加信息
width（数字）：视频的宽度
height（数字）：视频的高度
resolution（字符串）：宽度和高度的文字描述
tbr（数字）：音频和视频的平均比特率，以 KBit/s 为单位
abr（数字）：以 KBit/s 为单位的平均音频比特率
acodec（字符串）：正在使用的音频编解码器的名称
asr（数字）：以赫兹为单位的音频采样率
vbr（数字）：以 KBit/s 为单位的平均视频比特率
fps（数字）：帧速率
dynamic_range(string): 视频的动态范围
stretched_ratio(float):width:height视频的像素，如果不是正方形
vcodec（字符串）：正在使用的视频编解码器的名称
container（字符串）：容器格式的名称
filesize（数字）：字节数，如果事先知道的话
filesize_approx（数字）：估计字节数
protocol（字符串）：将用于实际下载的协议
extractor（字符串）：提取器的名称
extractor_key(string): 提取器的键名
epoch（数字）：信息提取完成时的 Unix 纪元
autonumber（数字）：每次下载都会增加的数字，从--autonumber-start
video_autonumber（数字）：每个视频都会增加的数字
n_entries（数字）：播放列表中提取的项目总数
playlist_id（字符串）：包含视频的播放列表的标识符
playlist_title（字符串）：包含视频的播放列表的名称
playlist（字符串）：playlist_id或playlist_title
playlist_count（数字）：播放列表中的项目总数。如果未提取整个播放列表，则可能不知道
playlist_index（数字）：播放列表中视频的索引，根据最终索引用前导零填充
playlist_autonumber（数字）：视频在播放列表下载队列中的位置，根据播放列表的总长度用前导零填充
playlist_uploader（字符串）：播放列表上传者的全名
playlist_uploader_id（字符串）：播放列表上传者的昵称或 ID
webpage_url（字符串）：视频网页的 URL，如果将其提供给 yt-dlp 应该允许再次获得相同的结果
webpage_url_basename（字符串）：网页 URL 的基本名称
webpage_url_domain(string): 网页 URL 的域
original_url（字符串）：用户给出的 URL（或与webpage_url播放列表条目相同）
适用于属于某个逻辑章节或章节的视频：

chapter（字符串）：视频所属章节的名称或标题
chapter_number（数字）：视频所属章节的编号
chapter_id（字符串）：视频所属章节的 ID
可用于作为某些系列或节目剧集的视频：

series（字符串）：视频剧集所属的系列或节目的标题
season（字符串）：视频剧集所属季节的标题
season_number（数字）：视频剧集所属的季节编号
season_id（字符串）：视频剧集所属季节的 ID
episode（字符串）：视频集的标题
episode_number（数字）：一个季节内的视频集数
episode_id（字符串）：视频片段的 ID
可用于作为曲目或音乐专辑一部分的媒体：

track（字符串）：曲目的标题
track_number（数字）：专辑或光盘中的曲目编号
track_id（字符串）：轨道的 ID
artist（字符串）：曲目的艺术家
genre（字符串）：曲目的流派
album（字符串）：曲目所属专辑的标题
album_type（字符串）：专辑的类型
album_artist（字符串）：专辑中出现的所有艺术家的列表
disc_number（数字）：轨道所属的光盘或其他物理介质的编号
release_year（数字）：专辑发行年份（YYYY）
仅在用于带有内部章节的视频时使用--download-sections和chapter:前缀时可用：--split-chapters

section_title（字符串）：章节的标题
section_number（数字）：文件中的章节编号
section_start（数字）：章节的开始时间，以秒为单位
section_end（数字）：章节的结束时间，以秒为单位
仅在用于--print：

urls(string): 所有请求格式的 URL，每行一个
filename（字符串）：视频文件的名称。请注意，由于后期处理，实际文件名可能会有所不同。用于--exec echo在所有后处理完成后获取名称
formats_table(table): 打印的视频格式表--list-formats
thumbnails_table(table)：缩略图格式的表格，由--list-thumbnails
subtitles_table(table): 打印的字幕格式表--list-subs
automatic_captions_table(table): 打印的自动字幕格式表--list-subs
仅适用于--sponsorblock-chapter-title：

start_time（数字）：章节的开始时间，以秒为单位
end_time（数字）：章节的结束时间，以秒为单位
categories（列表）：该章所属的 SponsorBlock 类别
category(string): 章节所属的最小 SponsorBlock 类别
category_names（列表）：类别的友好名称
name（字符串）：最小类别的友好名称
在输出模板中引用的每个上述序列将被与序列名称对应的实际值替换。例如，对于-o %(title)s-%(id)s.%(ext)s一个带有 titleyt-dlp test video和 id的 mp4 视频BaW_jenozKc，这将导致在yt-dlp test video-BaW_jenozKc.mp4当前目录中创建一个文件。

请注意，某些序列不能保证存在，因为它们取决于特定提取器获得的元数据。此类序列将替换为--output-na-placeholder(NA默认情况下) 提供的占位符值。

提示：查看-j输出以确定哪些字段可用于特定 URL

对于数字序列，您可以使用与数字相关的格式，例如，%(view_count)05d将产生一个字符串，其视图计数用零填充最多 5 个字符，例如 in 00042。

输出模板还可以包含任意分层路径，例如-o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"，这将导致将每个视频下载到与该路径模板对应的目录中。将自动为您创建任何缺少的目录。

要在输出模板中使用百分比文字，请使用%%. 要输出到标准输出，请使用-o -.

当前的默认模板是%(title)s [%(id)s].%(ext)s.

在某些情况下，您不希望使用中、空格或 & 等特殊字符，例如将下载的文件名传输到 Windows 系统或通过 8 位不安全通道传输文件名时。在这些情况下，添加--restrict-filenames标志以获得更短的标题。

输出模板和 Windows 批处理文件
如果您在 Windows 批处理文件中使用输出模板，则必须通过加倍来转义纯百分号 ( %)，这样-o "%(title)s-%(id)s.%(ext)s"应该变成-o "%%(title)s-%%(id)s.%%(ext)s". 但是，您不应该触摸%不是纯字符的 's，例如用于扩展的环境变量应该保持不变：-o "C:\%HOMEPATH%\Desktop\%%(title)s.%%(ext)s".

输出模板示例
$ yt-dlp --get-filename -o "test video.%(ext)s" BaW_jenozKc
test video.webm    # Literal name with correct extension

$ yt-dlp --get-filename -o "%(title)s.%(ext)s" BaW_jenozKc
youtube-dl test video ''_ä↭𝕐.webm    # All kinds of weird characters

$ yt-dlp --get-filename -o "%(title)s.%(ext)s" BaW_jenozKc --restrict-filenames
youtube-dl_test_video_.webm    # Restricted file name

# Download YouTube playlist videos in separate directory indexed by video order in a playlist
$ yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"

# Download YouTube playlist videos in separate directories according to their uploaded year
$ yt-dlp -o "%(upload_date>%Y)s/%(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"

# Prefix playlist index with " - " separator, but only if it is available
$ yt-dlp -o '%(playlist_index|)s%(playlist_index& - |)s%(title)s.%(ext)s' BaW_jenozKc "https://www.youtube.com/user/TheLinuxFoundation/playlists"

# Download all playlists of YouTube channel/user keeping each playlist in separate directory:
$ yt-dlp -o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/user/TheLinuxFoundation/playlists"

# Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
$ yt-dlp -u user -p password -P "~/MyVideos" -o "%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s" "https://www.udemy.com/java-tutorial"

# Download entire series season keeping each series and each season in separate directory under C:/MyVideos
$ yt-dlp -P "C:/MyVideos" -o "%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" "https://videomore.ru/kino_v_detalayah/5_sezon/367617"

# Download video as "C:\MyVideos\uploader\title.ext", subtitles as "C:\MyVideos\subs\uploader\title.ext"
# and put all temporary files in "C:\MyVideos\tmp"
$ yt-dlp -P "C:/MyVideos" -P "temp:tmp" -P "subtitle:subs" -o "%(uploader)s/%(title)s.%(ext)s" BaW_jenoz --write-subs

# Download video as "C:\MyVideos\uploader\title.ext" and subtitles as "C:\MyVideos\uploader\subs\title.ext"
$ yt-dlp -P "C:/MyVideos" -o "%(uploader)s/%(title)s.%(ext)s" -o "subtitle:%(uploader)s/subs/%(title)s.%(ext)s" BaW_jenozKc --write-subs

# Stream the video being downloaded to stdout
$ yt-dlp -o - BaW_jenozKc
格式选择
默认情况下，如果您不传递任何选项，yt-dlp 会尝试下载可用的最佳质量。这通常相当于使用-f bestvideo*+bestaudio/best. 但是，如果启用了多个音频流 ( --audio-multistreams)，则默认格式更改为-f bestvideo+bestaudio/best. 同样，如果 ffmpeg 不可用，或者您使用 yt-dlp 流式传输到stdout( -o -)，则默认变为-f best/bestvideo+bestaudio.

弃用警告：最新版本的 yt-dlp 可以使用 ffmpeg 同时将多种格式流式传输到标准输出。因此，在未来的版本中，默认值将设置为-f bv*+ba/b类似于正常下载。如果要保留-f b/bv+ba设置，建议在配置选项中明确指定。

格式选择的一般语法是-f FORMAT（或--format FORMAT）其中FORMAT是选择器表达式，即描述您要下载的一种或多种格式的表达式。

tl; dr： 导航到示例。

最简单的情况是请求特定格式，例如，-f 22您可以下载格式代码等于 22 的格式。您可以使用--list-formats或获取特定视频的可用格式代码列表-F。请注意，这些格式代码是特定于提取器的。

您还可以使用文件扩展名（目前支持3gp, aac, flv, m4a, mp3, mp4, ogg, wav, webm）下载作为单个文件的特定文件扩展名的最佳质量格式，例如-f webm将下载带有webm扩展名的最佳质量格式单个文件。

您可以使用-f -交互方式为每个视频提供格式选择器

您还可以使用特殊名称来选择特定的边缘情况格式：

all:分别选择所有格式
mergeall：选择并合并所有格式（必须与 一起使用--audio-multistreams，--video-multistreams或两者都使用）
b*, best*: 选择包含视频或音频或两者的最佳质量格式（即；vcodec!=none or acodec!=none）
b, best: 选择包含视频和音频的最佳质量格式。相当于best*[vcodec!=none][acodec!=none]
bv, bestvideo: 选择质量最好的纯视频格式。相当于best*[acodec=none]
bv*, bestvideo*: 选择包含视频的最佳质量格式。它也可能包含音频。相当于best*[vcodec!=none]
ba, bestaudio: 选择质量最好的纯音频格式。相当于best*[vcodec=none]
ba*, bestaudio*: 选择包含音频的最佳质量格式。它也可能包含视频。相当于best*[acodec!=none]（不要使用！）
w*, worst*: 选择包含视频或音频的最差质量格式
w, worst: 选择同时包含视频和音频的质量最差的格式。相当于worst*[vcodec!=none][acodec!=none]
wv, worstvideo: 选择质量最差的纯视频格式。相当于worst*[acodec=none]
wv*, worstvideo*: 选择包含视频的质量最差的格式。它也可能包含音频。相当于worst*[vcodec!=none]
wa, worstaudio: 选择质量最差的纯音频格式。相当于worst*[vcodec=none]
wa*, worstaudio*: 选择包含音频的质量最差的格式。它也可能包含视频。相当于worst*[acodec!=none]
For example, to download the worst quality video-only format you can use -f worstvideo. It is however recommended not to use worst and related options. When your format selector is worst, the format which is worst in all respects is selected. Most of the time, what you actually want is the video with the smallest filesize instead. So it is generally better to use -S +size or more rigorously, -S +size,+br,+res,+fps instead of -f worst. See Sorting Formats for more details.

You can select the n'th best format of a type by using best<type>.<n>. For example, best.2 will select the 2nd best combined format. Similarly, bv*.3 will select the 3rd best format that contains a video stream.

If you want to download multiple videos and they don't have the same formats available, you can specify the order of preference using slashes. Note that formats on the left hand side are preferred, for example -f 22/17/18 will download format 22 if it's available, otherwise it will download format 17 if it's available, otherwise it will download format 18 if it's available, otherwise it will complain that no suitable formats are available for download.

If you want to download several formats of the same video use a comma as a separator, e.g. -f 22,17,18 will download all these three formats, of course if they are available. Or a more sophisticated example combined with the precedence feature: -f 136/137/mp4/bestvideo,140/m4a/bestaudio.

You can merge the video and audio of multiple formats into a single file using -f <format1>+<format2>+... (requires ffmpeg installed), for example -f bestvideo+bestaudio will download the best video-only format, the best audio-only format and mux them together with ffmpeg.

Deprecation warning: Since the below described behavior is complex and counter-intuitive, this will be removed and multistreams will be enabled by default in the future. A new operator will be instead added to limit formats to single audio/video

Unless --video-multistreams is used, all formats with a video stream except the first one are ignored. Similarly, unless --audio-multistreams is used, all formats with an audio stream except the first one are ignored. For example, -f bestvideo+best+bestaudio --video-multistreams --audio-multistreams will download and merge all 3 given formats. The resulting file will have 2 video streams and 2 audio streams. But -f bestvideo+best+bestaudio --no-video-multistreams will download and merge only bestvideo and bestaudio. best is ignored since another format containing a video stream (bestvideo) has already been selected. The order of the formats is therefore important. -f best+bestaudio --no-audio-multistreams will download and merge both formats while -f bestaudio+best --no-audio-multistreams will ignore best and download only bestaudio.

Filtering Formats
You can also filter the video formats by putting a condition in brackets, as in -f "best[height=720]" (or -f "[filesize>10M]").

The following numeric meta fields can be used with comparisons <, <=, >, >=, = (equals), != (not equals):

filesize: The number of bytes, if known in advance
width: Width of the video, if known
height: Height of the video, if known
tbr: Average bitrate of audio and video in KBit/s
abr: Average audio bitrate in KBit/s
vbr: Average video bitrate in KBit/s
asr: Audio sampling rate in Hertz
fps: Frame rate
Also filtering work for comparisons = (equals), ^= (starts with), $= (ends with), *= (contains), ~= (matches regex) and following string meta fields:

ext: File extension
acodec: Name of the audio codec in use
vcodec: Name of the video codec in use
container: Name of the container format
protocol: The protocol that will be used for the actual download, lower-case (http, https, rtsp, rtmp, rtmpe, mms, f4m, ism, http_dash_segments, m3u8, or m3u8_native)
format_id: A short description of the format
language: Language code
Any string comparison may be prefixed with negation ! in order to produce an opposite comparison, e.g. !*= (does not contain). The comparand of a string comparison needs to be quoted with either double or single quotes if it contains spaces or special characters other than ._-.

Note that none of the aforementioned meta fields are guaranteed to be present since this solely depends on the metadata obtained by particular extractor, i.e. the metadata offered by the website. Any other field made available by the extractor can also be used for filtering.

Formats for which the value is not known are excluded unless you put a question mark (?) after the operator. You can combine format filters, so -f "[height<=?720][tbr>500]" selects up to 720p videos (or videos where the height is not known) with a bitrate of at least 500 KBit/s. You can also use the filters with all to download all formats that satisfy the filter. For example, -f "all[vcodec=none]" selects all audio-only formats.

Format selectors can also be grouped using parentheses, for example if you want to download the best pre-merged mp4 and webm formats with a height lower than 480 you can use -f "(mp4,webm)[height<480]".

Sorting Formats
You can change the criteria for being considered the best by using -S (--format-sort). The general format for this is --format-sort field1,field2....

The available fields are:

hasvid: Gives priority to formats that has a video stream
hasaud: Gives priority to formats that has a audio stream
ie_pref: The format preference
lang: The language preference
quality: The quality of the format
source: The preference of the source
proto: Protocol used for download (https/ftps > http/ftp > m3u8_native/m3u8 > http_dash_segments> websocket_frag > mms/rtsp > f4f/f4m)
vcodec: Video Codec (av01 > vp9.2 > vp9 > h265 > h264 > vp8 > h263 > theora > other)
acodec: Audio Codec (flac/alac > wav/aiff > opus > vorbis > aac > mp4a > mp3 > eac3 > ac3 > dts > other)
codec: Equivalent to vcodec,acodec
vext: Video Extension (mp4 > webm > flv > other). If --prefer-free-formats is used, webm is preferred.
aext: Audio Extension (m4a > aac > mp3 > ogg > opus > webm > other). If --prefer-free-formats is used, the order changes to opus > ogg > webm > m4a > mp3 > aac.
ext: Equivalent to vext,aext
filesize: Exact filesize, if known in advance
fs_approx: Approximate filesize calculated from the manifests
size: Exact filesize if available, otherwise approximate filesize
height: Height of video
width: Width of video
res: Video resolution, calculated as the smallest dimension.
fps: Framerate of video
hdr: The dynamic range of the video (DV > HDR12 > HDR10+ > HDR10 > HLG > SDR)
tbr: Total average bitrate in KBit/s
vbr: Average video bitrate in KBit/s
abr: Average audio bitrate in KBit/s
br: Equivalent to using tbr,vbr,abr
asr: Audio sample rate in Hz
Deprecation warning: Many of these fields have (currently undocumented) aliases, that may be removed in a future version. It is recommended to use only the documented field names.

All fields, unless specified otherwise, are sorted in descending order. To reverse this, prefix the field with a +. Eg: +res prefers format with the smallest resolution. Additionally, you can suffix a preferred value for the fields, separated by a :. Eg: res:720 prefers larger videos, but no larger than 720p and the smallest video if there are no videos less than 720p. For codec and ext, you can provide two preferred values, the first for video and the second for audio. Eg: +codec:avc:m4a (equivalent to +vcodec:avc,+acodec:m4a) sets the video codec preference to h264 > h265 > vp9 > vp9.2 > av01 > vp8 > h263 > theora and audio codec preference to mp4a > aac > vorbis > opus > mp3 > ac3 > dts. You can also make the sorting prefer the nearest values to the provided by using ~ as the delimiter. Eg: filesize~1G prefers the format with filesize closest to 1 GiB.

The fields hasvid and ie_pref are always given highest priority in sorting, irrespective of the user-defined order. This behaviour can be changed by using --format-sort-force. Apart from these, the default order used is: lang,quality,res,fps,hdr:12,codec:vp9.2,size,br,asr,proto,ext,hasaud,source,id. The extractors may override this default order, but they cannot override the user-provided order.

Note that the default has codec:vp9.2; i.e. av1 is not preferred. Similarly, the default for hdr is hdr:12; i.e. dolby vision is not preferred. These choices are made since DV and AV1 formats are not yet fully compatible with most devices. This may be changed in the future as more devices become capable of smoothly playing back these formats.

If your format selector is worst, the last item is selected after sorting. This means it will select the format that is worst in all respects. Most of the time, what you actually want is the video with the smallest filesize instead. So it is generally better to use -f best -S +size,+br,+res,+fps.

Tip: You can use the -v -F to see how the formats have been sorted (worst to best).

Format Selection examples
# Download and merge the best video-only format and the best audio-only format,
# or download the best combined format if video-only format is not available
$ yt-dlp -f "bv+ba/b"

# Download best format that contains video,
# and if it doesn't already have an audio stream, merge it with best audio-only format
$ yt-dlp -f "bv*+ba/b"

# Same as above
$ yt-dlp

# Download the best video-only format and the best audio-only format without merging them
# For this case, an output template should be used since
# by default, bestvideo and bestaudio will have the same file name.
$ yt-dlp -f "bv,ba" -o "%(title)s.f%(format_id)s.%(ext)s"

# Download and merge the best format that has a video stream,
# and all audio-only formats into one file
$ yt-dlp -f "bv*+mergeall[vcodec=none]" --audio-multistreams

# Download and merge the best format that has a video stream,
# and the best 2 audio-only formats into one file
$ yt-dlp -f "bv*+ba+ba.2" --audio-multistreams


# The following examples show the old method (without -S) of format selection
# and how to use -S to achieve a similar but (generally) better result

# Download the worst video available (old method)
$ yt-dlp -f "wv*+wa/w"

# Download the best video available but with the smallest resolution
$ yt-dlp -S "+res"

# Download the smallest video available
$ yt-dlp -S "+size,+br"



# Download the best mp4 video available, or the best video if no mp4 available
$ yt-dlp -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"

# Download the best video with the best extension
# (For video, mp4 > webm > flv. For audio, m4a > aac > mp3 ...)
$ yt-dlp -S "ext"



# Download the best video available but no better than 480p,
# or the worst video if there is no video under 480p
$ yt-dlp -f "bv*[height<=480]+ba/b[height<=480] / wv*+ba/w"

# Download the best video available with the largest height but no better than 480p,
# or the best video with the smallest resolution if there is no video under 480p
$ yt-dlp -S "height:480"

# Download the best video available with the largest resolution but no better than 480p,
# or the best video with the smallest resolution if there is no video under 480p
# Resolution is determined by using the smallest dimension.
# So this works correctly for vertical videos as well
$ yt-dlp -S "res:480"



# Download the best video (that also has audio) but no bigger than 50 MB,
# or the worst video (that also has audio) if there is no video under 50 MB
$ yt-dlp -f "b[filesize<50M] / w"

# Download largest video (that also has audio) but no bigger than 50 MB,
# or the smallest video (that also has audio) if there is no video under 50 MB
$ yt-dlp -f "b" -S "filesize:50M"

# Download best video (that also has audio) that is closest in size to 50 MB
$ yt-dlp -f "b" -S "filesize~50M"



# Download best video available via direct link over HTTP/HTTPS protocol,
# or the best video available via any protocol if there is no such video
$ yt-dlp -f "(bv*+ba/b)[protocol^=http][protocol!*=dash] / (bv*+ba/b)"

# Download best video available via the best protocol
# (https/ftps > http/ftp > m3u8_native > m3u8 > http_dash_segments ...)
$ yt-dlp -S "proto"



# Download the best video with either h264 or h265 codec,
# or the best video if there is no such video
$ yt-dlp -f "(bv*[vcodec~='^((he|a)vc|h26[45])']+ba) / (bv*+ba/b)"

# Download the best video with best codec no better than h264,
# or the best video with worst codec if there is no such video
$ yt-dlp -S "codec:h264"

# Download the best video with worst codec no worse than h264,
# or the best video with best codec if there is no such video
$ yt-dlp -S "+codec:h264"



# More complex examples

# Download the best video no better than 720p preferring framerate greater than 30,
# or the worst video (still preferring framerate greater than 30) if there is no such video
$ yt-dlp -f "((bv*[fps>30]/bv*)[height<=720]/(wv*[fps>30]/wv*)) + ba / (b[fps>30]/b)[height<=720]/(w[fps>30]/w)"

# Download the video with the largest resolution no better than 720p,
# or the video with the smallest resolution available if there is no such video,
# preferring larger framerate for formats with the same resolution
$ yt-dlp -S "res:720,fps"



# Download the video with smallest resolution no worse than 480p,
# or the video with the largest resolution available if there is no such video,
# preferring better codec and then larger total bitrate for the same resolution
$ yt-dlp -S "+res:480,codec,br"
MODIFYING METADATA
The metadata obtained by the extractors can be modified by using --parse-metadata and --replace-in-metadata

--replace-in-metadata FIELDS REGEX REPLACE is used to replace text in any metadata field using python regular expression. Backreferences can be used in the replace string for advanced use.

The general syntax of --parse-metadata FROM:TO is to give the name of a field or an output template to extract data from, and the format to interpret it as, separated by a colon :. Either a python regular expression with named capture groups or a similar syntax to the output template (only %(field)s formatting is supported) can be used for TO. The option can be used multiple times to parse and modify various fields.

Note that any field created by this can be used in the output template and will also affect the media file's metadata added when using --add-metadata.

This option also has a few special uses:

You can download an additional URL based on the metadata of the currently downloaded video. To do this, set the field additional_urls to the URL that you want to download. Eg: --parse-metadata "description:(?P<additional_urls>https?://www\.vimeo\.com/\d+) will download the first vimeo video found in the description

You can use this to change the metadata that is embedded in the media file. To do this, set the value of the corresponding field with a meta_ prefix. For example, any value you set to meta_description field will be added to the description field in the file. For example, you can use this to set a different "description" and "synopsis". To modify the metadata of individual streams, use the meta<n>_ prefix (Eg: meta1_language). Any value set to the meta_ field will overwrite all default values.

Note: Metadata modification happens before format selection, post-extraction and other post-processing operations. Some fields may be added or changed during these steps, overriding your changes.

For reference, these are the fields yt-dlp adds by default to the file metadata:

Metadata fields	From
title	track or title
date	upload_date
description, synopsis	description
purl, comment	webpage_url
track	track_number
artist	artist, creator, uploader or uploader_id
genre	genre
album	album
album_artist	album_artist
disc	disc_number
show	series
season_number	season_number
episode_id	episode or episode_id
episode_sort	episode_number
language of each stream	the format's language
Note: The file format may not support some of these fields

Modifying metadata examples
# Interpret the title as "Artist - Title"
$ yt-dlp --parse-metadata "title:%(artist)s - %(title)s"

# Regex example
$ yt-dlp --parse-metadata "description:Artist - (?P<artist>.+)"

# Set title as "Series name S01E05"
$ yt-dlp --parse-metadata "%(series)s S%(season_number)02dE%(episode_number)02d:%(title)s"

# Prioritize uploader as the "artist" field in video metadata
$ yt-dlp --parse-metadata "%(uploader|)s:%(meta_artist)s" --add-metadata

# Set "comment" field in video metadata using description instead of webpage_url,
# handling multiple lines correctly
$ yt-dlp --parse-metadata "description:(?s)(?P<meta_comment>.+)" --add-metadata

# Do not set any "synopsis" in the video metadata
$ yt-dlp --parse-metadata ":(?P<meta_synopsis>)"

# Remove "formats" field from the infojson by setting it to an empty string
$ yt-dlp --parse-metadata ":(?P<formats>)" -j

# Replace all spaces and "_" in title and uploader with a `-`
$ yt-dlp --replace-in-metadata "title,uploader" "[ _]" "-"
EXTRACTOR ARGUMENTS
Some extractors accept additional arguments which can be passed using --extractor-args KEY:ARGS. ARGS is a ; (semicolon) separated string of ARG=VAL1,VAL2. Eg: --extractor-args "youtube:player-client=android_embedded,web;include_live_dash" --extractor-args "funimation:version=uncut"

The following extractors use this feature:

youtube
skip: One or more of hls, dash or translated_subs to skip extraction of the m3u8 manifests, dash manifests and auto-translated subtitles respectively
player_client: Clients to extract video data from. The main clients are web, android and ios with variants _music, _embedded, _embedscreen, _creator (Eg: web_embedded); and mweb and tv_embedded (agegate bypass) with no variants. By default, android,web is used, but tv_embedded and creator variants are added as required for age-gated videos. Similarly the music variants are added for music.youtube.com urls. You can use all to use all the clients, and default for the default clients.
player_skip: Skip some network requests that are generally needed for robust extraction. One or more of configs (skip client configs), webpage (skip initial webpage), js (skip js player). While these options can help reduce the number of requests needed or avoid some rate-limiting, they could cause some issues. See #860 for more details
include_live_dash: Include live dash formats even without --live-from-start (These formats don't download properly)
comment_sort: top or new (default) - choose comment sorting mode (on YouTube's side)
max_comments: Limit the amount of comments to gather. Comma-separated list of integers representing max-comments,max-parents,max-replies,max-replies-per-thread. Default is all,all,all,all
E.g. all,all,1000,10 will get a maximum of 1000 replies total, with up to 10 replies per thread. 1000,all,100 will get a maximum of 1000 comments, with a maximum of 100 replies total
innertube_host: Innertube API host to use for all API requests
e.g. studio.youtube.com, youtubei.googleapis.com
Note: Cookies exported from www.youtube.com will not work with hosts other than *.youtube.com
innertube_key: Innertube API key to use for all API requests
youtubetab (YouTube playlists, channels, feeds, etc.)
skip: One or more of webpage (skip initial webpage download), authcheck (allow the download of playlists requiring authentication when no initial webpage is downloaded. This may cause unwanted behavior, see #1122 for more details)
approximate_date: Extract approximate upload_date in flat-playlist. This may cause date-based filters to be slightly off
funimation
language: Languages to extract. Eg: funimation:language=english,japanese
version: The video version to extract - uncut or simulcast
crunchyroll
language: Languages to extract. Eg: crunchyroll:language=jaJp
hardsub: Which hard-sub versions to extract. Eg: crunchyroll:hardsub=None,enUS
crunchyrollbeta
format: Which stream type(s) to extract. Default is adaptive_hls Eg: crunchyrollbeta:format=vo_adaptive_hls
Potentially useful values include adaptive_hls, adaptive_dash, vo_adaptive_hls, vo_adaptive_dash, download_hls, trailer_hls, trailer_dash
hardsub: Preference order for which hardsub versions to extract. Default is None (no hardsubs). Eg: crunchyrollbeta:hardsub=en-US,None
vikichannel
video_types: Types of videos to download - one or more of episodes, movies, clips, trailers
niconico
segment_duration: Segment duration in milliseconds for HLS-DMC formats. Use it at your own risk since this feature may result in your account termination.
youtubewebarchive
check_all: Try to check more at the cost of more requests. One or more of thumbnails, captures
gamejolt
comment_sort: hot (default), you (cookies needed), top, new - choose comment sorting mode (on GameJolt's side)
hotstar
res: resolution to ignore - one or more of sd, hd, fhd
vcodec: vcodec to ignore - one or more of h264, h265, dvh265
dr: dynamic range to ignore - one or more of sdr, hdr10, dv
tiktok
app_version: App version to call mobile APIs with - should be set along with manifest_app_version. (e.g. 20.2.1)
manifest_app_version: Numeric app version to call mobile APIs with. (e.g. 221)
rokfinchannel
tab: Which tab to download. One of new, top, videos, podcasts, streams, stacks. (E.g. rokfinchannel:tab=streams)
NOTE: These options may be changed/removed in the future without concern for backward compatibility

PLUGINS
Plugins are loaded from <root-dir>/ytdlp_plugins/<type>/__init__.py; where <root-dir> is the directory of the binary (<root-dir>/yt-dlp), or the root directory of the module if you are running directly from source-code (<root dir>/yt_dlp/__main__.py). Plugins are currently not supported for the pip version

Plugins can be of <type>s extractor or postprocessor. Extractor plugins do not need to be enabled from the CLI and are automatically invoked when the input URL is suitable for it. Postprocessor plugins can be invoked using --use-postprocessor NAME.

See ytdlp_plugins for example plugins.

Note that all plugins are imported even if not invoked, and that there are no checks performed on plugin code. Use plugins at your own risk and only if you trust the code

If you are a plugin author, add ytdlp-plugins as a topic to your repository for discoverability

EMBEDDING YT-DLP
yt-dlp makes the best effort to be a good command-line program, and thus should be callable from any programming language.

Your program should avoid parsing the normal stdout since they may change in future versions. Instead they should use options such as -J, --print, --progress-template, --exec etc to create console output that you can reliably reproduce and parse.

From a Python program, you can embed yt-dlp in a more powerful fashion, like this:

from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']
with YoutubeDL() as ydl:
    ydl.download(URLS)
Most likely, you'll want to use various options. For a list of options available, have a look at yt_dlp/YoutubeDL.py.

提示：如果您将代码从 youtube-dl 移植到 yt-dlp，需要注意的重要一点是我们不保证YoutubeDL.extract_infojson 的返回值是可序列化的，甚至是字典。它将类似于字典，但如果您想确保它是可序列化的字典，YoutubeDL.sanitize_info请按照以下示例所示传递它

嵌入示例
提取信息
import json
import yt_dlp

URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))
使用 info-json 下载
import yt_dlp

INFO_FILE = 'path/to/video.info.json'

with yt_dlp.YoutubeDL() as ydl:
    error_code = ydl.download_with_info_file(INFO_FILE)

print('Some videos failed to download' if error_code
      else 'All videos successfully downloaded')
提取音频
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
过滤视频
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < 60:
        return 'The video is too short'

ydl_opts = {
    'match_filter': longer_than_a_minute,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
添加记录器和进度挂钩
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')


ydl_opts = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
添加自定义后处理器
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

# ℹ️ See help(yt_dlp.postprocessor.PostProcessor)
class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info


with yt_dlp.YoutubeDL() as ydl:
    # ℹ️ "when" can take any value in yt_dlp.utils.POSTPROCESS_WHEN
    ydl.add_post_processor(MyCustomPP(), when='pre_process')
    ydl.download(URLS)
使用自定义格式选择器
import yt_dlp

URL = ['https://www.youtube.com/watch?v=BaW_jenozKc']

def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }


ydl_opts = {
    'format': format_selector,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
不推荐使用的选项
这些都是已弃用的选项和当前实现相同效果的替代方案

几乎多余的选项
虽然这些选项与新的选项几乎相同，但存在一些差异，防止它们变得多余

-j, --dump-json                  --print "%()j"
-F, --list-formats               --print formats_table
--list-thumbnails                --print thumbnails_table --print playlist:thumbnails_table
--list-subs                      --print automatic_captions_table --print subtitles_table
冗余选项
虽然这些选项是多余的，但由于易于使用，它们仍有望被使用

--get-description                --print description
--get-duration                   --print duration_string
--get-filename                   --print filename
--get-format                     --print format
--get-id                         --print id
--get-thumbnail                  --print thumbnail
-e, --get-title                  --print title
-g, --get-url                    --print urls
--match-title REGEX              --match-filter "title ~= (?i)REGEX"
--reject-title REGEX             --match-filter "title !~= (?i)REGEX"
--min-views COUNT                --match-filter "view_count >=? COUNT"
--max-views COUNT                --match-filter "view_count <=? COUNT"
--user-agent UA                  --add-header "User-Agent:UA"
--referer URL                    --add-header "Referer:URL"
--playlist-start NUMBER          -I NUMBER:
--playlist-end NUMBER            -I :NUMBER
--playlist-reverse               -I ::-1
--no-playlist-reverse            Default
不建议
虽然这些选项仍然有效，但不建议使用它们，因为还有其他替代方法可以实现相同的效果

--exec-before-download CMD       --exec "before_dl:CMD"
--no-exec-before-download        --no-exec
--all-formats                    -f all
--all-subs                       --sub-langs all --write-subs
--print-json                     -j --no-simulate
--autonumber-size NUMBER         Use string formatting. Eg: %(autonumber)03d
--autonumber-start NUMBER        Use internal field formatting like %(autonumber+NUMBER)s
--id                             -o "%(id)s.%(ext)s"
--metadata-from-title FORMAT     --parse-metadata "%(title)s:FORMAT"
--hls-prefer-native              --downloader "m3u8:native"
--hls-prefer-ffmpeg              --downloader "m3u8:ffmpeg"
--list-formats-old               --compat-options list-formats (Alias: --no-list-formats-as-table)
--list-formats-as-table          --compat-options -list-formats [Default] (Alias: --no-list-formats-old)
--youtube-skip-dash-manifest     --extractor-args "youtube:skip=dash" (Alias: --no-youtube-include-dash-manifest)
--youtube-skip-hls-manifest      --extractor-args "youtube:skip=hls" (Alias: --no-youtube-include-hls-manifest)
--youtube-include-dash-manifest  Default (Alias: --no-youtube-skip-dash-manifest)
--youtube-include-hls-manifest   Default (Alias: --no-youtube-skip-hls-manifest)
开发人员选项
这些选项不打算由最终用户使用

--test                           Download only part of video for testing extractors
--load-pages                     Load pages dumped by --write-pages
--youtube-print-sig-code         For testing youtube signatures
--allow-unplayable-formats       List unplayable formats also
--no-allow-unplayable-formats    Default
旧别名
这些是由于各种原因不再记录的别名

--avconv-location                --ffmpeg-location
--clean-infojson                 --clean-info-json
--cn-verification-proxy URL      --geo-verification-proxy URL
--dump-headers                   --print-traffic
--dump-intermediate-pages        --dump-pages
--force-write-download-archive   --force-write-archive
--load-info                      --load-info-json
--no-clean-infojson              --no-clean-info-json
--no-split-tracks                --no-split-chapters
--no-write-srt                   --no-write-subs
--prefer-unsecure                --prefer-insecure
--rate-limit RATE                --limit-rate RATE
--split-tracks                   --split-chapters
--srt-lang LANGS                 --sub-langs LANGS
--trim-file-names LENGTH         --trim-filenames LENGTH
--write-srt                      --write-subs
--yes-overwrites                 --force-overwrites
Sponskrub 选项
已弃用对SponSkrub的支持，转而支持这些--sponsorblock选项

--sponskrub                      --sponsorblock-mark all
--no-sponskrub                   --no-sponsorblock
--sponskrub-cut                  --sponsorblock-remove all
--no-sponskrub-cut               --sponsorblock-remove -all
--sponskrub-force                Not applicable
--no-sponskrub-force             Not applicable
--sponskrub-location             Not applicable
--sponskrub-args                 Not applicable
不再支持
这些选项可能不再按预期工作

--prefer-avconv                  avconv is not officially supported by yt-dlp (Alias: --no-prefer-ffmpeg)
--prefer-ffmpeg                  Default (Alias: --no-prefer-avconv)
-C, --call-home                  Not implemented
--no-call-home                   Default
--include-ads                    No longer supported
--no-include-ads                 Default
--write-annotations              No supported site has annotations now
--no-write-annotations           Default
--compat-options seperate-video-versions  No longer needed
已移除
这些选项自 2014 年以来已弃用，现在已完全删除

-A, --auto-number                -o "%(autonumber)s-%(id)s.%(ext)s"
-t, -l, --title, --literal       -o "%(title)s-%(id)s.%(ext)s"
贡献
有关打开问题和向项目贡献代码的说明，请参见CONTRIBUTING.md

更多的
有关常见问题解答，请参阅youtube-dl 自述文件