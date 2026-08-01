from typing import Literal #Might not actually be needed, but keeping it for now. (if not broken)
from pydantic import BaseModel, Field

#Edit's and changes based on feedback.
class ModerationResult(BaseModel):
    rationale: str = Field(description="Explanation for the moderation decision")

    @property
    def is_flagged(self) -> bool:
        # Base class: subclasses override this
        return False


class TextModerationResult(ModerationResult):
    contains_pii: bool = Field(description="Whether the text contains personally identifiable information")
    is_unfriendly: bool = Field(description="Whether the text contains unfriendly content")
    is_unprofessional: bool = Field(description="Whether the text contains unprofessional content")

    @property
    def is_flagged(self) -> bool:
        return (
            self.contains_pii
            or self.is_unfriendly
            or self.is_unprofessional
        )


class ImageModerationResult(ModerationResult):
    contains_pii: bool = Field(description="Whether the image contains personally identifiable information")
    is_disturbing: bool = Field(description="Whether the image contains disturbing content")
    is_low_quality: bool = Field(description="Whether the image is low quality")

    @property
    def is_flagged(self) -> bool:
        return (
            self.contains_pii
            or self.is_disturbing
            or self.is_low_quality
        )


class VideoModerationResult(ModerationResult):
    contains_pii: bool = Field(description="Whether the video contains personally identifiable information")
    is_disturbing: bool = Field(description="Whether the video contains disturbing content")
    is_low_quality: bool = Field(description="Whether the video is low quality")

    @property
    def is_flagged(self) -> bool:
        return (
            self.contains_pii
            or self.is_disturbing
            or self.is_low_quality
        )


class AudioModerationResult(ModerationResult):
    transcription: str = Field(description="Transcription of the audio content")
    contains_pii: bool = Field(description="Whether the audio contains personally identifiable information")
    is_unfriendly: bool = Field(description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(description="Whether unprofessional tone or content was detected")

    @property
    def is_flagged(self) -> bool:
        return (
            self.contains_pii
            or self.is_unfriendly
            or self.is_unprofessional
        )
