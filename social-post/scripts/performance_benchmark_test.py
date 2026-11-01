#!/usr/bin/env python3
"""Benchmark suite for payload transformation latency and calendar generation throughput."""

from __future__ import annotations

import time
import timeit
import hashlib
from typing import Any

from social_post_analysis import caption_counts, punctuation_profile
from social_validation import validate_posts


def analyzed_post() -> dict[str, Any]:
    caption = "同步貼文測試！"
    digest = hashlib.sha256(caption.encode("utf-8")).hexdigest()
    media_digest = hashlib.sha256(b"same-source-media").hexdigest()
    return {
        "schema_version": "1.0",
        "post_id": "post-schema-time-test",
        "published_at": "2026-08-30T10:00:00+08:00",
        "published_at_confidence": "high",
        "timezone": "Asia/Taipei",
        "platforms": ["facebook", "instagram"],
        "caption": caption,
        "caption_confidence": "high",
        "caption_sha256": digest,
        "analysis_status": "complete",
        "analysis_version": "schema-time-test-v1",
        "analysis_eligible": True,
        "analysis_evidence": "synthetic focused regression fixture",
        "content_type": "background_text_post",
        "format_features": {
            "surface": "facebook_background_text",
            "caption_layout": "single line",
            **caption_counts(caption),
            "emoji": 0,
            "explicit_cta": 0,
            "facebook_background_style": True,
            "background_color": "black",
            "text_color": "white",
            "text_weight": "bold",
            "alignment": "center",
            "rendered_line_count_observed": 1,
        },
        "wording_features": {
            "opening": caption,
            "hook": "同步貼文測試",
            "mechanism": "focused fixture",
            "differentiator": "focused fixture",
            "proof_style": "synthetic evidence",
            "cta": "無明確 CTA",
            "keywords": ["同步貼文"],
            "named_entities": [],
            "numbers_observed": [],
            "numeric_language": [],
            "voice": ["neutral"],
            "punctuation_style": ["standard"],
        },
        "publication_context": {
            "local_date": "2026-08-30",
            "weekday_zh_tw": "星期日",
            "local_time": "10:00",
            "daypart": "morning",
        }
    }


def benchmark_payload_transformation_latency() -> None:
    """Benchmark payload transformation latency (caption counts, punctuation profile, post validation)."""
    post = analyzed_post()
    caption = post["caption"]

    # Pre-allocate variables to isolate operation
    iterations = 5000

    def transform_payload():
        punctuation_profile(caption)
        caption_counts(caption)
        errors = []
        warnings = []
        validate_posts([post], errors, warnings)
        if errors:
            raise ValueError(f"Errors during validation: {errors}")

    elapsed = timeit.timeit(transform_payload, number=iterations)
    latency_ms = (elapsed / iterations) * 1000
    print(f"Payload Transformation Latency: {latency_ms:.3f} ms / operation")


def benchmark_calendar_generation_throughput() -> None:
    """Benchmark calendar generation throughput."""
    # Calendar generation is essentially batch processing multiple post validations and transformations over a period.
    # We will simulate a batch processing (e.g. 30 posts for a month calendar).
    posts = [analyzed_post() for _ in range(30)]

    # We add minor variations to make them distinct items
    for i, p in enumerate(posts):
        p["post_id"] = f"post-schema-time-test-{i}"

    iterations = 200

    def generate_calendar():
        errors = []
        warnings = []
        # validate the batch of posts
        validate_posts(posts, errors, warnings)
        if errors:
            raise ValueError(f"Errors during validation: {errors}")

    elapsed = timeit.timeit(generate_calendar, number=iterations)

    total_calendars_generated = iterations
    throughput = total_calendars_generated / elapsed
    print(f"Calendar Generation Throughput: {throughput:.2f} calendars / sec")


def main() -> int:
    print("Running Performance Benchmarks...")
    benchmark_payload_transformation_latency()
    benchmark_calendar_generation_throughput()
    print("Benchmarks completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
