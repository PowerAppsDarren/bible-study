# Exchange 03: What Winship content is online?

- **Timestamp:** 2026-06-12
- **Context:** User wants to download good Winship material; asks what's available online.

## User Input

I'd like to download some good content or material from Jamie Winship. what is available online for you to go get?

## AI Response

Surveyed what's out there and split it into three buckets, honestly flagging downloadable vs. stream-only vs. paywalled, plus a repo copyright caveat:

1. **Free + downloadable** — God Hears Her transcript PDF; written interviews I can fetch as markdown (Christianity Today *Where Ya From?*, Jennie Allen, City Gospel Movements, The God Journey #935).
2. **Free but stream-only** — The Jamie & Donna Winship Podcast; YouTube playlist; church sermons (Reston Bible, New Life Covenant); guest interviews. I can fetch show-notes/transcripts but not A/V.
3. **Paid / gated** — *Living Fearless*, *War of Worldviews*, the journal; Identity Exchange courses (Identity Method, Knowing Rediscovered, Becoming What You Believe), free starter tier.

⚠️ Repo note: `CONTRIBUTING.md` excludes copyrighted content from the shared layer — so save full text to `.personal/`, or save structured notes + links (copyright-safe). Then asked, via AskUserQuestion, **what** to pull and **where** it should land.

## Tool Calls

- `WebSearch` ×3 (Winship resources/podcasts/courses)
- `WebFetch` (Identity Method page earlier)
- `AskUserQuestion` (scope: PDF / articles / links index / structured notes; location: personal / shareable / don't save)

## Files Read/Modified

None (research only).
