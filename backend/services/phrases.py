import random
from models.schemas import GenerateRequest, Reply

# ══════════════════════════════════════════════════════════════
#  三层话术库：攻击类型 → 攻击场景 → 专属话术
# ══════════════════════════════════════════════════════════════

PHRASES = {

  # ── 质疑实力 ────────────────────────────────────────────────
  "ability": {
    "vocal": {  # 唱功场景
      "keywords": ["嗓子","唱","跑调","五音不全","难听","音准","破音","假唱","口型","音色"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="跑调是有，跑到你心里了对吗？不然怎么这么上心。"),
        Reply(style="犀利", emoji="🗡️", text="您这耳朵真灵，专门用来捕捉别人的缺点，建议去做音乐评委。"),
        Reply(style="犀利", emoji="🗡️", text="五音不全的人开得起演唱会，您五音俱全怎么只会在评论区发言？"),
        Reply(style="幽默", emoji="😄", text="跑调了？那是情绪太饱满，普通人的耳朵接收不了这种频率。"),
        Reply(style="幽默", emoji="😄", text="您说难听，可演唱会门票为什么还是秒没呢？奇怪。"),
        Reply(style="幽默", emoji="😄", text="建议您去ktv录一首发出来，让我们学习一下什么叫好听。"),
        Reply(style="有理", emoji="📊", text="现场演唱本就有瑕疵，能在万人场馆稳定发挥已属不易，您听的是录音室精修版吧？"),
        Reply(style="有理", emoji="📊", text="专业乐评人给出了正面评价，粉丝现场反响热烈，您一个人觉得难听，样本量有点小。"),
        Reply(style="有理", emoji="📊", text="音色审美因人而异，您不喜欢没关系，但"难听"是主观判断，不是客观事实。"),
      ]
    },
    "dance": {  # 舞台/舞蹈场景
      "keywords": ["跳舞","舞台","舞蹈","动作","节奏","跳","体力","肢体","卡点"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="舞台上跳两小时还能保持这体力，您站两小时都未必撑得住。"),
        Reply(style="犀利", emoji="🗡️", text="动作不整齐？您试试边唱边跳边记歌词边对镜位，看您整不整齐。"),
        Reply(style="犀利", emoji="🗡️", text="舞台表现力这种东西，真的不是每个人坐在手机屏幕后面都能懂的。"),
        Reply(style="幽默", emoji="😄", text="跳得不好？那为什么每次舞台cut都能上热搜呢，流量会说话。"),
        Reply(style="幽默", emoji="😄", text="挑剔舞台的人，通常自己连基本的律动感都没有，巧了。"),
        Reply(style="幽默", emoji="😄", text="卡点没卡准？您把节拍器拿来对一下，我觉得有问题的不是他。"),
        Reply(style="有理", emoji="📊", text="连续高强度巡演，每场保持高水准输出，这背后是日复一日的练习，不是您几个字能否定的。"),
        Reply(style="有理", emoji="📊", text="舞台综合表现包括感染力、配合度、现场应变，不是只看某一个动作对不对。"),
        Reply(style="有理", emoji="📊", text="同场演出的导演和编舞都给出了高度评价，您的标准比专业人士还高？"),
      ]
    },
    "act": {  # 演技场景
      "keywords": ["演技","表情","台词","尬","面瘫","木","戏","剧","角色","表演","哭戏"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="面瘫？还是您对演技的理解停留在夸张表情那个年代？"),
        Reply(style="犀利", emoji="🗡️", text="台词不好？请问您背过多少页台词、对过多少次戏？没有就别比。"),
        Reply(style="犀利", emoji="🗡️", text="说演技差的，能说出哪场戏哪个镜头具体差在哪吗？说不出就是说着玩的。"),
        Reply(style="幽默", emoji="😄", text="面瘫演员怎么让观众追着补这部剧的，您来解释一下？"),
        Reply(style="幽默", emoji="😄", text="哭戏不真实？我旁边的人都哭了，您没哭说明您心比较硬，不赖演员。"),
        Reply(style="幽默", emoji="😄", text="演技这东西，一千个人有一千个标准，您的标准刚好跟市场反向，挺独特的。"),
        Reply(style="有理", emoji="📊", text="这部剧播出后收视率和口碑数据都在，观众愿意为角色共情，这就是演技的结果。"),
        Reply(style="有理", emoji="📊", text="新人演员需要成长空间，拿着成熟演员的标准要求刚入行的人，本身就不公平。"),
        Reply(style="有理", emoji="📊", text="导演和对戏演员都公开肯定了他的专业态度，您在片场吗？"),
      ]
    },
    "general": {  # 通用实力质疑
      "keywords": [],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="实力会说话，成绩单摆在那里，您的嘴巴代替不了评委和观众。"),
        Reply(style="犀利", emoji="🗡️", text="批评可以，但麻烦先把标准说清楚，不然只是在发泄情绪而已。"),
        Reply(style="犀利", emoji="🗡️", text="您这么懂行，不知道自己上台表演一个？"),
        Reply(style="幽默", emoji="😄", text="哇，感谢您的专业点评，我担回头一定好好反思……才怪。"),
        Reply(style="幽默", emoji="😄", text="您说他不行，他偏偏就站在那个舞台上了，缘，妙不可言。"),
        Reply(style="有理", emoji="📊", text="喜不喜欢是个人口味，但把主观好恶包装成客观评价，这逻辑站不住脚。"),
      ]
    }
  },

  # ── 炒作营销 ────────────────────────────────────────────────
  "hype": {
    "capital": {  # 资本运作
      "keywords": ["资本","背景","关系","后台","钱","买","砸钱","投资方","公司"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="资本能买热度，买不来真实的观众缘，他现在的粉丝不是钱堆出来的。"),
        Reply(style="犀利", emoji="🗡️", text="有资本撑腰的艺人多了，为什么别人糊了他还在？您的逻辑漏洞有点大。"),
        Reply(style="犀利", emoji="🗡️", text="说靠资本的，能列举一下具体是哪个资本、做了什么操作吗？说不出来就是猜的。"),
        Reply(style="幽默", emoji="😄", text="那资本真的很慧眼啊，投了这么多人，偏偏押对了他，厉害。"),
        Reply(style="幽默", emoji="😄", text="靠资本出道的很多，大家都一样起点，为什么粉丝只认他？资本解释不了这个。"),
        Reply(style="有理", emoji="📊", text="娱乐圈没有公司运营的艺人几乎不存在，营销是行业惯例，问题是内容能不能撑起来，他的能。"),
      ]
    },
    "traffic": {  # 流量炒作
      "keywords": ["炒作","热搜","营销","买热搜","流量","蹭","话题","噱头"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="热搜可以买，但买不来真实的播放量和复购率，数据不会骗人。"),
        Reply(style="犀利", emoji="🗡️", text="炒作能带来一时热度，带不来长期陪伴，您低估粉丝的眼光了。"),
        Reply(style="犀利", emoji="🗡️", text="流量明星这顶帽子扣得很随意，请问您有具体的操作证据吗？"),
        Reply(style="幽默", emoji="😄", text="炒了这么多年还没糊，这'炒'的技术也是一绝啊，服了。"),
        Reply(style="幽默", emoji="😄", text="蹭热度？他自己就是热度，不需要借别人的。"),
        Reply(style="有理", emoji="📊", text="从作品到口碑，每个阶段都有真实成绩支撑，这不是营销堆出来的，是一步步做出来的。"),
      ]
    },
    "general": {
      "keywords": [],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="资本能捧人，但留不住人心，他的粉丝是靠作品一个个圈来的。"),
        Reply(style="幽默", emoji="😄", text="那您喜欢的爱豆是从石头缝里蹦出来的？娱乐圈哪个不需要运营？"),
        Reply(style="有理", emoji="📊", text="营销是工具，内容才是根本，没有作品支撑的热度早就散了。"),
      ]
    }
  },

  # ── 人品攻击 ────────────────────────────────────────────────
  "character": {
    "rumor": {  # 造谣诽谤
      "keywords": ["谣言","说","听说","据说","爆料","内幕","真相","黑料","瓜"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="'听说'两个字可以害死人，您传谣之前有没有核实过一条？"),
        Reply(style="犀利", emoji="🗡️", text="爆料要有实锤，没有实锤的叫诽谤，诽谤是要负法律责任的。"),
        Reply(style="犀利", emoji="🗡️", text="内幕？您在圈内工作吗？不在的话您的内幕从哪来的？"),
        Reply(style="幽默", emoji="😄", text="哦，您有直接证据？还是又是'一个朋友的朋友说的'？"),
        Reply(style="幽默", emoji="😄", text="这瓜我吃过，是假的，难为您还在传。"),
        Reply(style="有理", emoji="📊", text="谣言止于智者，没有可靠信源的爆料在传播链上每过一个人就多一分失真，请谨慎对待。"),
      ]
    },
    "attitude": {  # 态度/耍大牌
      "keywords": ["耍大牌","态度","傲","冷","不理","架子","脾气","怼","骂"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="大牌？有实力才叫大牌，您看见的'傲'可能只是他在保护自己的边界。"),
        Reply(style="犀利", emoji="🗡️", text="态度不好的具体事件是什么？时间地点经过，说清楚再评价。"),
        Reply(style="犀利", emoji="🗡️", text="您见过他本人吗？没见过凭什么说他态度差？道听途说不算数。"),
        Reply(style="幽默", emoji="😄", text="他工作人员、合作演员都说他好相处，偏您一个人说不好，是他的问题还是您的问题？"),
        Reply(style="幽默", emoji="😄", text="艺人也是人，有边界感正常，您是要他对谁都笑脸相迎才算好态度？"),
        Reply(style="有理", emoji="📊", text="长期合作的工作人员口碑、同剧组人员的公开发言都在，这些比一条没有来源的帖子可靠得多。"),
      ]
    },
    "general": {
      "keywords": [],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="造谣一张嘴，辟谣跑断腿，您说的这些有证据吗？"),
        Reply(style="犀利", emoji="🗡️", text="请对自己说出口的话负责，诽谤是要承担法律责任的。"),
        Reply(style="幽默", emoji="😄", text="网上说什么您信什么，这个习惯建议改一改。"),
        Reply(style="有理", emoji="📊", text="没有实锤的指控只是污蔑，请尊重基本的事实核查精神。"),
      ]
    }
  },

  # ── 外貌攻击 ────────────────────────────────────────────────
  "appearance": {
    "surgery": {  # 整容
      "keywords": ["整容","整","割","动刀","假","人工","医美","鼻子","眼睛","下巴"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="整容合法，整了又好看，您是在夸他还是在骂他？我没看出来。"),
        Reply(style="犀利", emoji="🗡️", text="您有他整容的医院记录吗？没有就是猜测，猜测不能当事实。"),
        Reply(style="犀利", emoji="🗡️", text="就算整了，关您什么事？您的脸是他整的吗？"),
        Reply(style="幽默", emoji="😄", text="整容？那医生技术真好，整出这种效果，帮我也问问在哪。"),
        Reply(style="幽默", emoji="😄", text="天生好看叫天赋，后天变好看叫努力，两种他都没问题。"),
        Reply(style="有理", emoji="📊", text="外貌改变有很多原因：生长发育、化妆技术、打光、减重，下整容结论需要医学证据。"),
      ]
    },
    "looks": {  # 直接嘲外貌
      "keywords": ["丑","难看","土","油腻","邋遢","胖","瘦","矮","高","脸","身材"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="以容貌论英雄，您的审美标准停留在哪个年代？"),
        Reply(style="犀利", emoji="🗡️", text="嘲讽别人外貌，这是您能拿出手的最高水平了吗？"),
        Reply(style="犀利", emoji="🗡️", text="他长什么样是父母给的，您用来攻击别人的嘴也是父母给的，谁更丢人？"),
        Reply(style="幽默", emoji="😄", text="长相这件事，妈生的，您要有意见去找他父母投诉。"),
        Reply(style="幽默", emoji="😄", text="您觉得他不好看，但他的照片为什么还是存满了我手机？"),
        Reply(style="有理", emoji="📊", text="外貌从来不是衡量一个艺人价值的标准，作品和态度才是，您攻击错方向了。"),
      ]
    },
    "general": {
      "keywords": [],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="他靠脸吃饭也好、靠才华吃饭也好，和您有什么关系？"),
        Reply(style="幽默", emoji="😄", text="以您的审美标准，全世界好看的人应该不超过十个吧。"),
        Reply(style="有理", emoji="📊", text="容貌焦虑是社会问题，用外貌攻击他人只会加剧这种伤害。"),
      ]
    }
  },

  # ── 黑粉丝群 ────────────────────────────────────────────────
  "fans": {
    "behavior": {  # 粉丝行为
      "keywords": ["脑残","粉丝","饭圈","追星","控评","举报","打投","集资","应援"],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="用粉丝行为攻击偶像本人，这逻辑您自己觉得通吗？"),
        Reply(style="犀利", emoji="🗡️", text="任何群体都有素质参差的个体，以偏概全是认知偏差，不是分析。"),
        Reply(style="犀利", emoji="🗡️", text="饭圈问题真实存在，但和您跑来骂人有什么关系？您是来解决问题的吗？"),
        Reply(style="幽默", emoji="😄", text="哦，我们粉丝让您这么上心，感谢您的持续关注。"),
        Reply(style="幽默", emoji="😄", text="粉丝圈子里的事我们自己讨论，您一个外人操这个心干嘛？"),
        Reply(style="有理", emoji="📊", text="粉丝行为代表不了艺人本身，这是最基本的逻辑，请不要混淆。"),
      ]
    },
    "general": {
      "keywords": [],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="黑粉丝群来恶心偶像，这招数也太老套了。"),
        Reply(style="幽默", emoji="😄", text="我们粉丝什么样，不需要您来定义。"),
        Reply(style="有理", emoji="📊", text="我们大多数粉丝只是安静喜欢，不劳您费心贴标签。"),
      ]
    }
  },

  # ── 其他 ────────────────────────────────────────────────────
  "other": {
    "general": {
      "keywords": [],
      "replies": [
        Reply(style="犀利", emoji="🗡️", text="您的攻击我收到了，但说实话，一点也不痛。"),
        Reply(style="犀利", emoji="🗡️", text="来黑我担之前，建议先想清楚自己在说什么。"),
        Reply(style="犀利", emoji="🗡️", text="花时间黑一个与您毫无关系的人，这时间成本值得吗？"),
        Reply(style="幽默", emoji="😄", text="谢谢您为我担贡献了一波热度，辛苦了！"),
        Reply(style="幽默", emoji="😄", text="您说完了吗？说完了我们继续喜欢他。"),
        Reply(style="幽默", emoji="😄", text="哇，您对他的关注度比我这个粉丝还高呢。"),
        Reply(style="有理", emoji="📊", text="不喜欢可以不关注，特意来发表攻击性言论，动机值得深思。"),
        Reply(style="有理", emoji="📊", text="每个人都有喜欢或不喜欢某人的权利，但请保持基本尊重。"),
        Reply(style="有理", emoji="📊", text="您的意见我们已收到，但改变不了我们喜欢他这件事。"),
      ]
    }
  }
}

# ══════════════════════════════════════════════════════════════
#  关键词匹配逻辑
# ══════════════════════════════════════════════════════════════

def _match_scene(attack_type: str, text: str) -> str:
    """在攻击类型下匹配最贴切的场景"""
    scenes = PHRASES.get(attack_type, PHRASES["other"])
    for scene_name, scene_data in scenes.items():
        if scene_name == "general":
            continue
        keywords = scene_data.get("keywords", [])
        if any(kw in text for kw in keywords):
            return scene_name
    return "general"


def _detect_type(text: str) -> str:
    """根据关键词判断攻击类型"""
    type_keywords = {
        "ability":    ["唱","跳","演","实力","水平","差","不行","嗓","舞","台词","演技","卡点"],
        "hype":       ["炒","营销","买","资本","关系","背景","后台","热搜","流量","蹭"],
        "character":  ["人品","渣","骗","假","耍大牌","态度","脾气","谣","爆料","黑料"],
        "appearance": ["丑","难看","整容","脸","身材","胖","瘦","土","油腻","矮"],
        "fans":       ["粉丝","脑残","饭圈","追星","控评","集资"],
    }
    scores = {t: 0 for t in type_keywords}
    for atype, kws in type_keywords.items():
        for kw in kws:
            if kw in text:
                scores[atype] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "other"


def _pick_three(replies: list, style: str) -> list:
    """按风格各取一条，凑够3条"""
    style_map = {"sharp": "犀利", "humor": "幽默", "logic": "有理"}

    if style != "mixed":
        zh = style_map.get(style, "犀利")
        pool = [r for r in replies if r.style == zh]
        return random.sample(pool, min(3, len(pool))) if pool else random.sample(replies, min(3, len(replies)))

    result = []
    for s in ["犀利", "幽默", "有理"]:
        candidates = [r for r in replies if r.style == s]
        if candidates:
            result.append(random.choice(candidates))
    return result


async def generate_replies(req: GenerateRequest) -> list[Reply]:
    """精准三层匹配，返回3条专属回复"""

    # 确定攻击类型
    if req.mode == "paste" and req.content:
        atype = _detect_type(req.content)
        scene = _match_scene(atype, req.content)
    else:
        atype = req.attack_type or "other"
        scene = "general"

    # 取场景话术，不够则合并同类型其他场景补充
    scenes = PHRASES.get(atype, PHRASES["other"])
    pool = list(scenes.get(scene, scenes["general"])["replies"])

    if len(pool) < 3:
        for s_name, s_data in scenes.items():
            if s_name != scene:
                pool += s_data["replies"]

    replies = _pick_three(pool, req.style or "mixed")

    # 替换偶像名字
    if req.idol_name:
        name = req.idol_name
        replaced = []
        for r in replies:
            replaced.append(Reply(
                style=r.style,
                emoji=r.emoji,
                text=r.text.replace("我担", name).replace("他", name),
            ))
        return replaced

    return replies