"""
services/phrases.py
本地话术库，按攻击类型分类，随机返回3条
"""
import random
from models.schemas import GenerateRequest, Reply

PHRASES = {
    "ability": [
        Reply(style="犀利", emoji="🗡️", text="实力会说话，成绩单摆在那里，您的嘴巴代替不了评委和观众。"),
        Reply(style="犀利", emoji="🗡️", text="批评可以，但麻烦先把标准说清楚，不然只是在发泄情绪而已。"),
        Reply(style="犀利", emoji="🗡️", text="您这么懂行，不知道自己上台表演一个？"),
        Reply(style="幽默", emoji="😄", text="哇，感谢您的专业点评，我担回头一定好好反思您这番话……才怪。"),
        Reply(style="幽默", emoji="😄", text="您说他不行，他偏偏就站在那个舞台上了，缘，妙不可言。"),
        Reply(style="幽默", emoji="😄", text="您的审美我尊重，毕竟每个人都有喜欢发表意见的权利嘛。"),
        Reply(style="有理", emoji="📊", text="他的专辑销量、演出评分、行业奖项都在那里，数据不会骗人。"),
        Reply(style="有理", emoji="📊", text="实力是需要时间积累的，您看到的只是一个截面，不是全貌。"),
        Reply(style="有理", emoji="📊", text="喜不喜欢是个人口味，但把主观好恶包装成客观评价，这逻辑站不住脚。"),
    ],
    "hype": [
        Reply(style="犀利", emoji="🗡️", text="资本能捧人，但留不住人心，他的粉丝是靠作品一个个圈来的。"),
        Reply(style="犀利", emoji="🗡️", text="娱乐圈靠资本运作的多了，为什么偏偏只有他留下来了？"),
        Reply(style="犀利", emoji="🗡️", text="炒作能带来一时热度，带不来长期陪伴，您低估粉丝的眼光了。"),
        Reply(style="幽默", emoji="😄", text="那您喜欢的爱豆是从石头缝里蹦出来的？娱乐圈哪个不需要运营？"),
        Reply(style="幽默", emoji="😄", text="炒作炒了这么多年还没糊，这'炒'的技术也是一绝啊。"),
        Reply(style="幽默", emoji="😄", text="承认他红让您难受是吧，没关系，我理解的。"),
        Reply(style="有理", emoji="📊", text="营销是工具，内容才是根本，没有作品支撑的热度早就散了。"),
        Reply(style="有理", emoji="📊", text="从出道到现在，每个阶段都有代表作，这不是资本能堆出来的。"),
        Reply(style="有理", emoji="📊", text="您所说的'炒作'，我们叫做正常的职业规划和宣传推广。"),
    ],
    "character": [
        Reply(style="犀利", emoji="🗡️", text="造谣一张嘴，辟谣跑断腿，您说的这些有证据吗？"),
        Reply(style="犀利", emoji="🗡️", text="请对自己说出口的话负责，诽谤是要承担法律责任的。"),
        Reply(style="犀利", emoji="🗡️", text="您对他的了解来自哪里？道听途说和亲眼所见差距很大。"),
        Reply(style="幽默", emoji="😄", text="哦，您认识他本人？不然这人品鉴定书是从哪里开出来的？"),
        Reply(style="幽默", emoji="😄", text="网上说什么您信什么，这个习惯建议改一改。"),
        Reply(style="幽默", emoji="😄", text="我担人品如何，他身边的人最清楚，您算哪位？"),
        Reply(style="有理", emoji="📊", text="人品评价需要建立在事实基础上，请提供具体事件和可靠来源。"),
        Reply(style="有理", emoji="📊", text="他多次参与公益活动，工作人员口碑有目共睹，谣言经不起推敲。"),
        Reply(style="有理", emoji="📊", text="没有实锤的指控只是污蔑，请尊重基本的事实核查精神。"),
    ],
    "appearance": [
        Reply(style="犀利", emoji="🗡️", text="以容貌论英雄，您的审美标准停留在哪个年代？"),
        Reply(style="犀利", emoji="🗡️", text="他靠脸吃饭也好、靠才华吃饭也好，和您有什么关系？"),
        Reply(style="犀利", emoji="🗡️", text="嘲讽别人外貌，这是您能拿出手的最高水平了吗？"),
        Reply(style="幽默", emoji="😄", text="长相这件事，妈生的，您要有意见去找他父母投诉。"),
        Reply(style="幽默", emoji="😄", text="您觉得他不好看，但他的照片为什么还是存满了我手机？"),
        Reply(style="幽默", emoji="😄", text="以您的审美标准，全世界好看的人应该不超过十个吧。"),
        Reply(style="有理", emoji="📊", text="外貌从来不是衡量一个艺人价值的标准，作品和态度才是。"),
        Reply(style="有理", emoji="📊", text="容貌焦虑是社会问题，用外貌攻击他人只会加剧这种伤害。"),
        Reply(style="有理", emoji="📊", text="他的粉丝喜欢他，从来不只是因为外表，您理解不了很正常。"),
    ],
    "fans": [
        Reply(style="犀利", emoji="🗡️", text="黑粉丝群来恶心偶像，这招数也太老套了。"),
        Reply(style="犀利", emoji="🗡️", text="我们粉丝什么样，不需要您来定义。"),
        Reply(style="犀利", emoji="🗡️", text="用粉丝行为攻击偶像本人，这逻辑您自己觉得通吗？"),
        Reply(style="幽默", emoji="😄", text="哦，我们粉丝让您这么上心，感谢您的持续关注。"),
        Reply(style="幽默", emoji="😄", text="粉圈是有些问题，但和您来这里发言有什么关系呢？"),
        Reply(style="幽默", emoji="😄", text="您这么了解我们，要不要考虑入坑？"),
        Reply(style="有理", emoji="📊", text="任何群体都有良莠不齐的个体，以偏概全是认知偏差。"),
        Reply(style="有理", emoji="📊", text="粉丝行为代表不了艺人本身，这是最基本的逻辑。"),
        Reply(style="有理", emoji="📊", text="我们大多数粉丝只是安静喜欢，不劳您费心贴标签。"),
    ],
    "other": [
        Reply(style="犀利", emoji="🗡️", text="您的攻击我收到了，但说实话，一点也不痛。"),
        Reply(style="犀利", emoji="🗡️", text="来黑我担之前，建议先想清楚自己在说什么。"),
        Reply(style="犀利", emoji="🗡️", text="花时间黑一个与您毫无关系的人，这时间成本值得吗？"),
        Reply(style="幽默", emoji="😄", text="谢谢您为我担贡献了一波热度，辛苦了！"),
        Reply(style="幽默", emoji="😄", text="您说完了吗？说完了我们继续喜欢他。"),
        Reply(style="幽默", emoji="😄", text="哇，您对他的关注度比我这个粉丝还高呢。"),
        Reply(style="有理", emoji="📊", text="不喜欢可以不关注，特意来发表攻击性言论，动机值得深思。"),
        Reply(style="有理", emoji="📊", text="每个人都有喜欢或不喜欢某人的权利，但请保持基本尊重。"),
        Reply(style="有理", emoji="📊", text="您的意见我们已收到，但改变不了我们喜欢他这件事。"),
    ],
}

# paste 模式：关键词匹配攻击类型
KEYWORDS = {
    "ability":   ["唱", "跳", "演技", "实力", "水平", "差", "不行", "垃圾", "难听", "五音不全"],
    "hype":      ["炒作", "营销", "买", "资本", "关系", "背景", "潜规则", "走后门"],
    "character": ["人品", "渣", "骗", "假", "虚伪", "耍大牌", "态度", "劣迹"],
    "appearance":["丑", "难看", "整容", "脸", "身材", "胖", "瘦", "土"],
    "fans":      ["粉丝", "粉圈", "脑残粉", "饭圈", "追星"],
}


def _detect_type(text: str) -> str:
    """根据关键词猜测攻击类型"""
    for atype, words in KEYWORDS.items():
        if any(w in text for w in words):
            return atype
    return "other"


def _pick_three(pool: list[Reply], style: str) -> list[Reply]:
    """按风格筛选，每种风格取1条，凑够3条"""
    if style != "mixed":
        style_map = {"sharp": "犀利", "humor": "幽默", "logic": "有理"}
        zh = style_map.get(style, "犀利")
        filtered = [r for r in pool if r.style == zh]
        return random.sample(filtered, min(3, len(filtered))) or random.sample(pool, 3)

    result = []
    for s in ["犀利", "幽默", "有理"]:
        candidates = [r for r in pool if r.style == s]
        if candidates:
            result.append(random.choice(candidates))
    return result


async def generate_replies(req: GenerateRequest) -> list[Reply]:
    """从话术库里取3条回复，瞬间返回"""
    if req.mode == "paste" and req.content:
        atype = _detect_type(req.content)
    else:
        atype = req.attack_type or "other"

    pool = PHRASES.get(atype, PHRASES["other"])
    
    # 如果有偶像名字，把"我担"替换成真实名字
    replies = _pick_three(pool, req.style or "mixed")
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